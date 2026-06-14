from unittest.mock import patch, MagicMock
from src.models import Paciente, Medicamento
from src.persistence import salvar_dados, carregar_dados

@patch("src.persistence.get_supabase_client")
def test_carregar_dados_nuvem_sucesso(mock_get_supabase):
    """Garante que a reconstrução do prontuário e seus medicamentos a partir do banco em nuvem funciona."""
    # 1. PREPARAÇÃO: Configuração dos dublês do cliente de banco de dados
    mock_client = MagicMock()
    mock_get_supabase.return_value = mock_client
    
    mock_table_pacientes = MagicMock()
    mock_table_medicamentos = MagicMock()
    
    # Efeito colateral para direcionar as ações baseadas no nome da tabela consultada
    def table_side_effect(table_name):
        if table_name == "pacientes":
            return mock_table_pacientes
        elif table_name == "medicamentos":
            return mock_table_medicamentos
        return MagicMock()
        
    mock_client.table.side_effect = table_side_effect
    
    # Simula o retorno da tabela de pacientes (.select().order().limit().execute())
    mock_table_pacientes.select.return_value.order.return_value.limit.return_value.execute.return_value.data = [
        {"id": 12, "nome": "Carlos Silva"}
    ]
    
    # Simula o retorno da tabela de medicamentos associados (.select().eq().execute())
    mock_table_medicamentos.select.return_value.eq.return_value.execute.return_value.data = [
        {"nome": "Ibuprofeno", "dosagem_mg": 400.0, "turno": "Tarde", "instrucoes": "Com alimentos"}
    ]

    # 2. AÇÃO: Dispara a busca lógica na camada de persistência
    paciente_recuperado = carregar_dados()

    # 3. VALIDAÇÃO: Verifica se as payloads relacionais foram convertidas corretamente para objetos
    assert paciente_recuperado is not None
    assert paciente_recuperado.nome == "Carlos Silva"
    assert paciente_recuperado.id_bd == 12
    assert len(paciente_recuperado.medicamentos) == 1
    assert paciente_recuperado.medicamentos[0].nome == "Ibuprofeno"
    assert paciente_recuperado.medicamentos[0].dosagem_mg == 400.0
    assert paciente_recuperado.medicamentos[0].turno == "Tarde"


@patch("src.persistence.get_supabase_client")
def test_salvar_dados_nuvem_sucesso(mock_get_supabase):
    """Garante que o ciclo de sincronização (limpeza de registros antigos e inserção do novo estado) é disparado."""
    # 1. PREPARAÇÃO: Instanciação dos modelos locais que serão sincronizados
    paciente = Paciente(nome="Carlos Silva")
    remedio = Medicamento(nome="Ibuprofeno", dosagem_mg=400, turno="Tarde", instrucoes="Com alimentos")
    paciente.adicionar_medicamento(remedio)

    mock_client = MagicMock()
    mock_get_supabase.return_value = mock_client
    
    mock_table_pacientes = MagicMock()
    mock_table_medicamentos = MagicMock()
    
    def table_side_effect(table_name):
        if table_name == "pacientes":
            return mock_table_pacientes
        elif table_name == "medicamentos":
            return mock_table_medicamentos
        return MagicMock()
        
    mock_client.table.side_effect = table_side_effect
    
    # Simula o cenário onde o paciente já existe no PostgreSQL e retorna seu ID primário
    mock_table_pacientes.select.return_value.eq.return_value.execute.return_value.data = [{"id": 12}]

    # 2. AÇÃO: Executa a sincronização com o ecossistema externo mockado
    salvar_dados(paciente)

    # 3. VALIDAÇÃO: Certifica que o motor executou as etapas cruciais de segurança
    # Verifica se buscou a existência do paciente
    assert mock_table_pacientes.select.called 
    # Verifica se executou o Soft/Hard Wipe dos medicamentos antigos do paciente para evitar duplicidade
    assert mock_table_medicamentos.delete.called 
    # Verifica se injetou o novo estado clínico atualizado
    assert mock_table_medicamentos.insert.called