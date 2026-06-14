from src.models import Paciente, Medicamento
from src.database import get_supabase_client

def carregar_dados(*args, **kwargs) -> Paciente | None:
    """
    Busca o último paciente cadastrado na nuvem (Supabase) e reconstrói 
    o objeto Paciente junto com seus respectivos medicamentos.
    
    Aceita argumentos genéricos (*args, **kwargs) para manter compatibilidade
    com chamadas legadas que tentam passar caminhos de arquivos locais.
    """
    try:
        supabase = get_supabase_client()
        
        # Consulta o último paciente inserido na tabela (simulando o arquivo único de antes)
        resposta = supabase.table("pacientes").select("*").order("id", desc=True).limit(1).execute()
        
        if not resposta.data:
            return None
            
        dados_paciente = resposta.data[0]
        paciente = Paciente(nome=dados_paciente["nome"])
        paciente.id_bd = dados_paciente["id"]  # Injeta o ID do banco dinamicamente no objeto
        
        # Busca todos os medicamentos atrelados a este paciente específico
        resp_meds = supabase.table("medicamentos").select("*").eq("paciente_id", paciente.id_bd).execute()
        
        for m in resp_meds.data:
            medicamento_reconstruido = Medicamento(
                nome=m["nome"],
                dosagem_mg=m["dosagem_mg"],
                turno=m["turno"],
                instrucoes=m.get("instrucoes", "")
            )
            paciente.adicionar_medicamento(medicamento_reconstruido)
            
        return paciente
    except Exception:
        # Se o banco estiver vazio, sem internet ou tabelas não criadas, 
        # retorna None de forma segura para ativar a tela de primeiro acesso.
        return None

def salvar_dados(paciente: Paciente, *args, **kwargs):
    """
    Sincroniza o prontuário local e seus medicamentos com o banco PostgreSQL em nuvem.
    
    Aplica uma operação de limpeza (delete) nos medicamentos antigos antes de persistir
    a lista atual, garantindo comportamento idêntico ao efeito de sobrescrita (overwrite) do JSON.
    """
    try:
        supabase = get_supabase_client()
        
        # 1. Verifica se o paciente já tem ID vinculado ou se já existe no banco por nome
        if not hasattr(paciente, "id_bd") or paciente.id_bd is None:
            existe = supabase.table("pacientes").select("*").eq("nome", paciente.nome).execute()
            if existe.data:
                paciente.id_bd = existe.data[0]["id"]
            else:
                # Cria o registro do paciente se ele for inédito
                novo = supabase.table("pacientes").insert({"nome": paciente.nome}).execute()
                paciente.id_bd = novo.data[0]["id"]
        
        # 2. Limpa o histórico de medicamentos do banco antes de salvar o estado atualizado
        supabase.table("medicamentos").delete().eq("paciente_id", paciente.id_bd).execute()
        
        # 3. Salva a lista de medicamentos atual na tabela nuvem
        for med in paciente.medicamentos:
            supabase.table("medicamentos").insert({
                "paciente_id": paciente.id_bd,
                "nome": med.nome,
                "dosagem_mg": med.dosagem_mg,
                "turno": med.turno,
                "instrucoes": med.instrucoes if med.instrucoes else ""
            }).execute()
            
    except Exception as e:
        raise RuntimeError(f"Falha na sincronização dos dados com a infraestrutura em nuvem: {e}")