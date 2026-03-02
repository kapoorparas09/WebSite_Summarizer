from openai import OpenAI
from config import OLLAMA_BASE_URL

def get_client():
    return OpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")