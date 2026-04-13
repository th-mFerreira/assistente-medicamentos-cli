import json
import os
from src.models import Paciente, Medicamento

# Esse é o arquivo de texto onde as informações vão morar
ARQUIVO_PADRAO = "banco_medicamentos.json"

def salvar_dados(paciente: Paciente, caminho_arquivo: str = ARQUIVO_PADRAO):
    # Pega todos os medicamentos e transforma no formato que o JSON entende
    lista_medicamentos = [med.to_dict() for med in paciente.medicamentos]
    
    dados_completos = {
        "nome_paciente": paciente.nome,
        "medicamentos": lista_medicamentos
    }
    
    # Cria (ou atualiza) o arquivo garantindo que acentos funcionem (utf-8)
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados_completos, arquivo, ensure_ascii=False, indent=4)

def carregar_dados(caminho_arquivo: str = ARQUIVO_PADRAO) -> Paciente:
    # Se o arquivo não existe (primeira vez rodando), retorna None
    if not os.path.exists(caminho_arquivo):
        return None
        
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        
    # Reconstrói o paciente e os medicamentos a partir do texto lido
    paciente = Paciente(nome=dados["nome_paciente"])
    for med in dados["medicamentos"]:
        medicamento_reconstruido = Medicamento(
            nome=med["nome"],
            dosagem_mg=med["dosagem_mg"],
            turno=med["turno"],
            instrucoes=med.get("instrucoes", "")
        )
        paciente.adicionar_medicamento(medicamento_reconstruido)
        
    return paciente