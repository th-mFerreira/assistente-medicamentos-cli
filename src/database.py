import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

def get_supabase_client() -> Client:

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def get_supabase_client() -> Client:
    """Instancia e retorna o cliente de comunicação com o Supabase."""

    url = os.environ.get("https://qlrwqzyztxwhuqkzwpzk.supabase.co")
    key = os.environ.get("sb_publishable_LNjB1Cvb6L2Yz5vlX2crAg_cscvCLJw")
    
    if not url or not key:
        raise ValueError("Credenciais do Supabase ausentes no ambiente de execução.")
        
    return create_client(url, key)