import pytest
from unittest.mock import patch
from src.api import buscar_endereco_por_cep

# O @patch é o diretor de cena chamando o dublê para substituir o 'requests.get'
@patch("src.api.requests.get")
def test_buscar_endereco_sucesso(mock_get):
    # 1. PREPARAÇÃO: Ensinando o dublê o que ele deve responder
    mock_resposta = mock_get.return_value
    mock_resposta.raise_for_status.return_value = None # Finge que não deu erro 404
    mock_resposta.json.return_value = {
        "cep": "01001-000",
        "logradouro": "Praça da Sé",
        "bairro": "Sé",
        "localidade": "São Paulo",
        "uf": "SP"
    }

    # 2. AÇÃO: Chamamos a nossa função (ela acha que está indo para a internet, mas bate no dublê)
    dados = buscar_endereco_por_cep("01001000")

    # 3. VALIDAÇÃO: Garantimos que o nosso código leu os dados do ViaCEP corretamente
    assert dados["logradouro"] == "Praça da Sé"
    assert dados["localidade"] == "São Paulo"
    assert dados["uf"] == "SP"
    
    # Verifica se a requisição GET foi de fato disparada pela nossa função
    mock_get.assert_called_once() 

def test_buscar_endereco_cep_invalido():
    # Testa se a aplicação bloqueia um CEP com letras ou tamanho errado antes de ir pra internet
    with pytest.raises(ValueError, match="CEP inválido"):
        buscar_endereco_por_cep("12345") # CEP muito curto
        
    with pytest.raises(ValueError, match="CEP inválido"):
        buscar_endereco_por_cep("ABCDEFGH") # CEP com letras