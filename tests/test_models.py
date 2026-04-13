import pytest
from src.models import Medicamento

def test_criar_medicamento_valido():
    # Caminho feliz: testa se um medicamento normal é criado sem erros
    remedio = Medicamento(nome="Dipirona", dosagem_mg=500, turno="Qualquer")
    assert remedio.nome == "Dipirona"
    assert remedio.dosagem_mg == 500

def test_erro_dosagem_negativa():
    # Caminho de erro: o sistema DEVE dar erro se a dose for zero ou negativa
    with pytest.raises(ValueError, match="A dosagem deve ser maior que zero"):
        Medicamento(nome="Rivotril", dosagem_mg=-10, turno="Noite")

def test_erro_turno_invalido():
    # Caso limite: turno que não existe
    with pytest.raises(ValueError, match="Turno inválido"):
        Medicamento(nome="Paracetamol", dosagem_mg=750, turno="Madrugada")