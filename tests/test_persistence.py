import os
from src.models import Paciente, Medicamento
from src.persistence import salvar_dados, carregar_dados

def test_salvar_e_carregar_json():
    # 1. Preparamos los datos
    arquivo_teste = "banco_teste.json"
    paciente = Paciente(nome="Carlos Silva")
    remedio = Medicamento(nome="Ibuprofeno", dosagem_mg=400, turno="Tarde", instrucoes="Com alimentos")
    paciente.adicionar_medicamento(remedio)

    # 2. Guardamos los datos en el archivo
    salvar_dados(paciente, caminho_arquivo=arquivo_teste)

    # 3. Verificamos que el archivo físico realmente se creó en tu disco duro
    assert os.path.exists(arquivo_teste) is True

    # 4. Cargamos los datos de vuelta desde el archivo
    paciente_recuperado = carregar_dados(caminho_arquivo=arquivo_teste)

    # 5. Validamos que la información no se perdió ni se alteró
    assert paciente_recuperado.nome == "Carlos Silva"
    assert len(paciente_recuperado.medicamentos) == 1
    assert paciente_recuperado.medicamentos[0].nome == "Ibuprofeno"
    assert paciente_recuperado.medicamentos[0].dosagem_mg == 400

    # 6. Limpiamos nuestra "basura" (borramos el archivo de prueba)
    if os.path.exists(arquivo_teste):
        os.remove(arquivo_teste)