import requests

def buscar_endereco_por_cep(cep: str) -> dict:
    """Busca um endereço na API pública do ViaCEP."""
    # Limpa o CEP tirando traços e espaços
    cep_limpo = cep.replace("-", "").strip()
    
    if len(cep_limpo) != 8 or not cep_limpo.isdigit():
        raise ValueError("CEP inválido. Digite exatamente 8 números.")
        
    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    
    try:
        # Faz a requisição GET para a API
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status() # Verifica se a internet caiu ou deu erro 404
        
        dados = resposta.json()
        
        if "erro" in dados:
            raise ValueError("CEP não encontrado na base dos Correios.")
            
        return dados
    except requests.exceptions.RequestException:
        raise ConnectionError("Falha ao comunicar com o servidor do ViaCEP. Verifique sua internet.")