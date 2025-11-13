"""
Módulo para implementar busca híbrida (BM25 + Semântica)
Combina busca por palavras-chave com busca semântica para melhor precisão
"""

from typing import List

try:
    from langchain_community.retrievers import BM25Retriever
    from langchain.retrievers import EnsembleRetriever

    HAS_BM25 = True
except ImportError:
    HAS_BM25 = False
    print("⚠️ rank-bm25 não instalado. Busca híbrida não disponível.")
    print("   Instale com: pip install rank-bm25")

from langchain_chroma import Chroma
from langchain_core.documents import Document

from .config import Config


def create_hybrid_retriever(
    vector_store: Chroma, documents: List[Document], k: int = None
):
    """
    Cria um retriever híbrido que combina busca semântica e BM25

    Args:
        vector_store: Vector store com embeddings semânticos
        documents: Lista de todos os documentos (necessário para BM25)
        k: Número de documentos a recuperar (usa Config.K_RETRIEVER se None)

    Returns:
        EnsembleRetriever configurado (ou retriever padrão se BM25 não disponível)

    Exemplo:
        >>> retriever = create_hybrid_retriever(vector_store, all_docs)
        >>> results = retriever.invoke("Como cadastrar EPI?")
    """
    if not HAS_BM25:
        print("⚠️  BM25 não disponível, usando retriever padrão")
        return vector_store.as_retriever(
            search_type="similarity", search_kwargs={"k": k or Config.K_RETRIEVER}
        )

    if k is None:
        k = Config.K_RETRIEVER

    # 1. Retriever Semântico (ChromaDB)
    # Busca documentos semanticamente similares usando embeddings
    semantic_retriever = vector_store.as_retriever(
        search_type="similarity", search_kwargs={"k": k}
    )

    # 2. Retriever BM25 (Palavras-chave)
    # Busca documentos que contenham as palavras exatas da query
    bm25_retriever = BM25Retriever.from_documents(documents)
    bm25_retriever.k = k

    # 3. Ensemble Retriever (Combina ambos)
    # Usa pesos para balancear os dois tipos de busca
    # 0.6 = 60% semântica, 0.4 = 40% BM25
    ensemble_retriever = EnsembleRetriever(
        retrievers=[semantic_retriever, bm25_retriever],
        weights=[0.6, 0.4],  # Ajuste esses pesos conforme necessário
    )

    return ensemble_retriever


def create_mmr_retriever(vector_store: Chroma, k: int = None, fetch_k: int = None):
    """
    Cria um retriever usando MMR (Maximal Marginal Relevance)
    MMR retorna documentos relevantes mas DIVERSOS (evita redundância)

    Args:
        vector_store: Vector store com embeddings
        k: Número de documentos finais a retornar
        fetch_k: Número de documentos a buscar antes de aplicar MMR

    Returns:
        Retriever configurado com MMR

    Exemplo:
        >>> retriever = create_mmr_retriever(vector_store, k=4, fetch_k=20)
        >>> results = retriever.invoke("Como entregar EPI?")
    """
    if k is None:
        k = Config.K_RETRIEVER

    if fetch_k is None:
        fetch_k = k * 3  # Busca 3x mais e depois filtra

    mmr_retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": k,
            "fetch_k": fetch_k,
            "lambda_mult": 0.5,  # 0 = máxima diversidade, 1 = máxima relevância
        },
    )

    return mmr_retriever


def get_retriever_with_score(vector_store: Chroma, k: int = None):
    """
    Retorna documentos com scores de similaridade

    Args:
        vector_store: Vector store
        k: Número de documentos a recuperar

    Returns:
        Lista de tuplas (Document, score)

    Exemplo:
        >>> docs_with_scores = get_retriever_with_score(vector_store, k=4)
        >>> for doc, score in docs_with_scores:
        >>>     print(f"Score: {score:.3f} - {doc.page_content[:100]}")
    """
    if k is None:
        k = Config.K_RETRIEVER

    def retriever_func(query: str):
        return vector_store.similarity_search_with_score(query, k=k)

    return retriever_func
