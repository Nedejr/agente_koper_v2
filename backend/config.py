"""
Configurações centralizadas do backend
"""

import os

from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()


class Config:
    """Classe de configuração centralizada"""

    # OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # ChromaDB
    PERSIST_DIR = os.getenv("PERSIST_DIR", "db")

    # Modelos disponíveis
    AVAILABLE_MODELS = ["gpt-5-nano"]
    DEFAULT_MODEL = "gpt-5-nano"

    # Processamento de documentos
    # Otimizado: chunks menores e mais focados melhoram precisão
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "200"))

    # Temperatura do modelo
    # Otimizado: mais baixo para respostas mais determinísticas
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.1"))

    # Retriever - Quantidade de chunks a recuperar
    # Otimizado: 6 chunks oferecem melhor contexto sem overhead
    K_RETRIEVER = int(os.getenv("K_RETRIEVER", "6"))

    # Configurações avançadas de retrieval
    K_BEFORE_RERANK = int(
        os.getenv("K_BEFORE_RERANK", "12")
    )  # Busca mais antes de reranquear
    MAX_CONTEXT_TOKENS = int(os.getenv("MAX_CONTEXT_TOKENS", "3000"))

    # Features opcionais
    ENABLE_HYBRID_SEARCH = os.getenv("ENABLE_HYBRID_SEARCH", "False").lower() == "true"
    ENABLE_RERANKING = os.getenv("ENABLE_RERANKING", "False").lower() == "true"
    USE_LOCAL_EMBEDDINGS = os.getenv("USE_LOCAL_EMBEDDINGS", "False").lower() == "true"

    @classmethod
    def validate(cls):
        """Valida se as configurações obrigatórias estão presentes"""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY não configurada no .env")
        return True


# Configura a chave da OpenAI no ambiente
if Config.OPENAI_API_KEY:
    os.environ["OPENAI_API_KEY"] = Config.OPENAI_API_KEY
