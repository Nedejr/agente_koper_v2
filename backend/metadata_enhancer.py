"""
Módulo para enriquecer metadados dos documentos
Melhora a capacidade de filtrar e recuperar documentos relevantes
"""

import re
from typing import List

from langchain_core.documents import Document


def extract_module_from_filename(filename: str) -> str:
    """
    Extrai o nome do módulo a partir do nome do arquivo

    Args:
        filename: Nome do arquivo (ex: "Passo a passo - Módulo de RH_documentacao_gerada.md")

    Returns:
        Nome do módulo (ex: "RH")

    Exemplo:
        >>> extract_module_from_filename("Passo a passo - Módulo de Qualidade_documentacao_gerada.md")
        'Qualidade'
    """
    # Remove sufixo _documentacao_gerada antes de processar
    filename = filename.replace("_documentacao_gerada", "")

    # Padrões comuns nos nomes de arquivo
    patterns = [
        r"Módulo de (\w+)",  # "Módulo de RH"
        r"Módulo (\w+)",  # "Módulo Financeiro"
        r"módulo[_-](\w+)",  # "modulo_rh" ou "modulo-rh"
    ]

    for pattern in patterns:
        match = re.search(pattern, filename, re.IGNORECASE)
        if match:
            module_name = match.group(1).capitalize()
            # Mapeamento de nomes especiais
            module_mapping = {
                "Armazenamento": "Armazenamento",
                "Compras": "Compras",
                "Engenharia": "Engenharia",
                "Financeiro": "Financeiro",
                "Qualidade": "Qualidade",
                "Rh": "RH",
                "Suprimentos": "Suprimentos",
            }
            return module_mapping.get(module_name, module_name)

    return "Desconhecido"


def extract_section_info(content: str) -> dict:
    """
    Extrai informações de seção do conteúdo markdown

    Args:
        content: Conteúdo do chunk

    Returns:
        Dicionário com informações da seção
    """
    info = {"section_title": None, "section_level": None, "has_steps": False}

    # Extrai título da seção (## Título)
    section_match = re.search(r"^(#{1,6})\s+(.+)$", content, re.MULTILINE)
    if section_match:
        info["section_level"] = len(section_match.group(1))
        info["section_title"] = section_match.group(2).strip()

    # Verifica se tem passo a passo
    if re.search(r"^\d+\.\s+\*\*", content, re.MULTILINE) or re.search(
        r"Passo a Passo", content, re.IGNORECASE
    ):
        info["has_steps"] = True

    return info


def extract_keywords(content: str, top_n: int = 10) -> List[str]:
    """
    Extrai palavras-chave importantes do conteúdo

    Args:
        content: Conteúdo do chunk
        top_n: Número máximo de palavras-chave a retornar

    Returns:
        Lista de palavras-chave
    """
    # Remove markdown e pontuação
    clean_content = re.sub(r"[#*`\[\]()]", "", content)

    # Lista de stopwords em português (simplificada)
    stopwords = {
        "o",
        "a",
        "os",
        "as",
        "um",
        "uma",
        "de",
        "do",
        "da",
        "dos",
        "das",
        "em",
        "no",
        "na",
        "nos",
        "nas",
        "para",
        "por",
        "com",
        "sem",
        "sobre",
        "ao",
        "à",
        "aos",
        "às",
        "e",
        "ou",
        "mas",
        "que",
        "é",
        "são",
        "foi",
        "ser",
        "está",
        "como",
        "mais",
        "se",
        "você",
    }

    # Extrai palavras
    words = re.findall(r"\b[a-záàâãéèêíïóôõöúçñ]{3,}\b", clean_content.lower())

    # Filtra stopwords e conta frequência
    word_freq = {}
    for word in words:
        if word not in stopwords:
            word_freq[word] = word_freq.get(word, 0) + 1

    # Retorna as top_n mais frequentes
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return [word for word, freq in sorted_words[:top_n]]


def enhance_document_metadata(doc: Document) -> Document:
    """
    Enriquece os metadados de um documento

    Args:
        doc: Documento original

    Returns:
        Documento com metadados enriquecidos

    Exemplo:
        >>> doc = Document(page_content="...", metadata={"source": "file.md"})
        >>> enhanced_doc = enhance_document_metadata(doc)
        >>> print(enhanced_doc.metadata["module"])
        'RH'
    """
    # Extrai módulo do nome do arquivo
    source_file = doc.metadata.get("source", "")
    module = extract_module_from_filename(source_file)
    doc.metadata["module"] = module

    # Extrai informações da seção
    section_info = extract_section_info(doc.page_content)
    doc.metadata.update(section_info)

    # Extrai palavras-chave
    keywords = extract_keywords(doc.page_content, top_n=5)
    doc.metadata["keywords"] = ", ".join(keywords)

    # Adiciona tamanho do conteúdo
    doc.metadata["content_length"] = len(doc.page_content)

    # Verifica presença de mídia
    has_video = "[video:" in doc.page_content
    has_image = "[image:" in doc.page_content
    doc.metadata["has_video"] = has_video
    doc.metadata["has_image"] = has_image

    return doc


def enhance_documents_batch(documents: List[Document]) -> List[Document]:
    """
    Enriquece metadados de uma lista de documentos

    Args:
        documents: Lista de documentos

    Returns:
        Lista de documentos com metadados enriquecidos

    Exemplo:
        >>> docs = [doc1, doc2, doc3]
        >>> enhanced_docs = enhance_documents_batch(docs)
    """
    return [enhance_document_metadata(doc) for doc in documents]


def filter_documents_by_module(
    documents: List[Document], module_name: str
) -> List[Document]:
    """
    Filtra documentos por módulo

    Args:
        documents: Lista de documentos
        module_name: Nome do módulo (ex: "RH", "Qualidade")

    Returns:
        Lista de documentos do módulo especificado

    Exemplo:
        >>> rh_docs = filter_documents_by_module(all_docs, "RH")
    """
    return [
        doc
        for doc in documents
        if doc.metadata.get("module", "").lower() == module_name.lower()
    ]


def get_document_statistics(documents: List[Document]) -> dict:
    """
    Retorna estatísticas sobre os documentos

    Args:
        documents: Lista de documentos

    Returns:
        Dicionário com estatísticas

    Exemplo:
        >>> stats = get_document_statistics(all_docs)
        >>> print(stats["modules"])
        {'RH': 45, 'Qualidade': 38, 'Financeiro': 42}
    """
    stats = {
        "total_documents": len(documents),
        "modules": {},
        "has_video": 0,
        "has_image": 0,
        "avg_content_length": 0,
    }

    total_length = 0

    for doc in documents:
        # Conta por módulo
        module = doc.metadata.get("module", "Desconhecido")
        stats["modules"][module] = stats["modules"].get(module, 0) + 1

        # Conta mídias
        if doc.metadata.get("has_video"):
            stats["has_video"] += 1
        if doc.metadata.get("has_image"):
            stats["has_image"] += 1

        # Soma tamanhos
        total_length += doc.metadata.get("content_length", 0)

    if documents:
        stats["avg_content_length"] = total_length // len(documents)

    return stats
