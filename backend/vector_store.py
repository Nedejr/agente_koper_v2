"""
Módulo responsável pelo gerenciamento do vector store (ChromaDB)
"""

import os
from typing import List, Optional

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

from .config import Config


def _ensure_directory_permissions(directory: str):
    """
    Garante que o diretório e seus arquivos tenham permissões adequadas

    Args:
        directory: Caminho do diretório
    """
    try:
        import stat

        # Define permissões de leitura/escrita para o usuário
        if os.path.exists(directory):
            # Permissões para o diretório: rwxr-xr-x (0o755)
            os.chmod(
                directory,
                stat.S_IRWXU
                | stat.S_IRGRP
                | stat.S_IXGRP
                | stat.S_IROTH
                | stat.S_IXOTH,
            )

            # Permissões para todos os arquivos dentro: rw-r--r-- (0o644)
            for root, dirs, files in os.walk(directory):
                for d in dirs:
                    dir_path = os.path.join(root, d)
                    os.chmod(
                        dir_path,
                        stat.S_IRWXU
                        | stat.S_IRGRP
                        | stat.S_IXGRP
                        | stat.S_IROTH
                        | stat.S_IXOTH,
                    )
                for f in files:
                    file_path = os.path.join(root, f)
                    os.chmod(
                        file_path,
                        stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH,
                    )
    except Exception as e:
        print(f"⚠️ Aviso: Não foi possível ajustar permissões: {e}")


def get_persist_dir() -> str:
    """
    Retorna o diretório de persistência do ChromaDB

    Returns:
        Caminho do diretório
    """
    return Config.PERSIST_DIR


def load_existing_vector_store() -> Optional[Chroma]:
    """
    Carrega um vector store existente do disco

    Returns:
        Instância do Chroma se existir, None caso contrário
    """
    persist_directory = get_persist_dir()

    if os.path.exists(persist_directory) and os.listdir(persist_directory):
        try:
            # Verifica e corrige permissões do diretório
            _ensure_directory_permissions(persist_directory)

            vector_store = Chroma(
                persist_directory=persist_directory,
                embedding_function=OpenAIEmbeddings(),
            )

            # Tenta fazer uma operação de leitura para validar o banco
            try:
                vector_store._collection.count()
            except Exception as count_error:
                print(f"⚠️ Banco de dados corrompido ou readonly: {count_error}")
                print("🔄 Removendo banco corrompido...")
                delete_vector_store()
                return None

            return vector_store
        except Exception as e:
            print(f"❌ Erro ao carregar vector store: {e}")
            # Se houver erro, tenta limpar o banco corrompido
            try:
                print("🔄 Tentando remover banco corrompido...")
                delete_vector_store()
            except Exception as cleanup_error:
                print(f"⚠️ Erro ao limpar banco: {cleanup_error}")
            return None

    return None


def create_vector_store(chunks: List[Document], batch_size: int = 100) -> Chroma:
    """
    Cria um novo vector store a partir de chunks de documentos.
    Processa em lotes para evitar limite de tokens da API.

    Args:
        chunks: Lista de documentos
        batch_size: Tamanho do lote para processamento (padrão: 100)

    Returns:
        Instância do Chroma
    """
    persist_directory = get_persist_dir()

    # Garante que o diretório existe com permissões corretas
    if not os.path.exists(persist_directory):
        os.makedirs(persist_directory, mode=0o777, exist_ok=True)
        print(f"✅ Diretório criado: {persist_directory}")

    _ensure_directory_permissions(persist_directory)

    # Verifica permissões antes de criar
    stats = os.stat(persist_directory)
    print(f"📊 Permissões do diretório: {oct(stats.st_mode)[-3:]}")

    try:
        print(f"🔮 Criando ChromaDB com {len(chunks)} chunks em lotes de {batch_size}...")

        # Cria o vector store com o primeiro lote
        first_batch = chunks[:batch_size]
        vector_store = Chroma.from_documents(
            documents=first_batch,
            embedding=OpenAIEmbeddings(),
            persist_directory=persist_directory,
        )
        print(f"  ✓ Lote 1/{(len(chunks) + batch_size - 1) // batch_size} processado ({len(first_batch)} chunks)")

        # Adiciona os lotes restantes
        for i in range(batch_size, len(chunks), batch_size):
            batch = chunks[i:i + batch_size]
            batch_num = (i // batch_size) + 1
            total_batches = (len(chunks) + batch_size - 1) // batch_size
            
            vector_store.add_documents(batch)
            print(f"  ✓ Lote {batch_num}/{total_batches} processado ({len(batch)} chunks)")

        # Verifica se o banco foi criado corretamente
        count = vector_store._collection.count()
        print(f"✅ ChromaDB criado! Total de documentos: {count}")

        return vector_store
    except Exception as e:
        print(f"❌ Erro ao criar vector store: {e}")
        # Tenta limpar se houver erro
        try:
            delete_vector_store()
        except Exception:
            pass
        raise


def add_to_vector_store(
    chunks: List[Document], vector_store: Optional[Chroma] = None, batch_size: int = 100
) -> Chroma:
    """
    Adiciona documentos a um vector store existente ou cria um novo.
    Processa em lotes para evitar limite de tokens da API.
    Se encontrar um banco readonly ou corrompido, remove e recria.

    Args:
        chunks: Lista de documentos para adicionar
        vector_store: Vector store existente (opcional)
        batch_size: Tamanho do lote para processamento (padrão: 100)

    Returns:
        Instância do Chroma (existente ou novo)
    """
    if vector_store:
        try:
            # Tenta adicionar ao vector store existente em lotes
            print(f"➕ Adicionando {len(chunks)} chunks em lotes de {batch_size}...")
            
            for i in range(0, len(chunks), batch_size):
                batch = chunks[i:i + batch_size]
                batch_num = (i // batch_size) + 1
                total_batches = (len(chunks) + batch_size - 1) // batch_size
                
                vector_store.add_documents(batch)
                print(f"  ✓ Lote {batch_num}/{total_batches} adicionado ({len(batch)} chunks)")

            # Verifica se a adição foi bem-sucedida
            count = vector_store._collection.count()
            print(f"✅ Chunks adicionados! Total de documentos: {count}")

            return vector_store
        except Exception as e:
            error_msg = str(e).lower()
            print(f"❌ Erro ao adicionar documentos: {e}")

            # Verifica se é erro de readonly ou database error
            if (
                "readonly" in error_msg
                or "database error" in error_msg
                or "1032" in error_msg
            ):
                print("🔄 Banco de dados readonly detectado. Recriando...")
            else:
                print("🔄 Erro desconhecido. Tentando recriar o vector store...")

            # Remove o banco corrompido/readonly e recria
            try:
                delete_vector_store()
                print("✅ Banco antigo removido")
            except Exception as del_error:
                print(f"⚠️ Aviso ao remover banco: {del_error}")
                # Tenta forçar a remoção
                persist_directory = get_persist_dir()
                if os.path.exists(persist_directory):
                    import shutil
                    import stat

                    try:
                        # Muda permissões recursivamente
                        for root, dirs, files in os.walk(persist_directory):
                            for d in dirs:
                                os.chmod(os.path.join(root, d), stat.S_IRWXU)
                            for f in files:
                                os.chmod(os.path.join(root, f), stat.S_IRWXU)
                        shutil.rmtree(persist_directory)
                        print("✅ Banco removido forçadamente")
                    except Exception as force_error:
                        print(f"❌ Erro ao forçar remoção: {force_error}")
                        raise Exception(
                            "Não foi possível remover o banco corrompido. "
                            "Por favor, feche o Streamlit e remova manualmente a pasta 'chroma_db'."
                        )

            # Recria o vector store
            try:
                return create_vector_store(chunks)
            except Exception as recreate_error:
                print(f"❌ Erro ao recriar vector store: {recreate_error}")
                raise
    else:
        # Cria um novo vector store
        return create_vector_store(chunks)


def delete_vector_store():
    """
    Remove completamente o vector store do disco
    """
    persist_directory = get_persist_dir()

    if os.path.exists(persist_directory):
        import shutil

        try:
            shutil.rmtree(persist_directory)
            print(f"✅ Vector store removido: {persist_directory}")
        except Exception as e:
            print(f"❌ Erro ao remover vector store: {e}")
            raise


def check_and_repair_vector_store() -> Optional[Chroma]:
    """
    Verifica a integridade do vector store e tenta repará-lo se necessário

    Returns:
        Instância do Chroma se válida, None caso contrário
    """
    persist_directory = get_persist_dir()

    if not os.path.exists(persist_directory):
        return None

    try:
        # Tenta carregar o vector store
        vector_store = load_existing_vector_store()

        if vector_store:
            # Tenta uma operação de leitura para validar
            count = vector_store._collection.count()
            print(f"✅ Vector store válido com {count} documentos")
            return vector_store
        else:
            return None

    except Exception as e:
        print(f"❌ Vector store corrompido: {e}")
        print("🔄 Removendo banco corrompido...")
        try:
            delete_vector_store()
        except Exception:
            pass
        return None


def get_vector_store_stats(vector_store: Optional[Chroma]) -> dict:
    """
    Retorna estatísticas sobre o vector store

    Args:
        vector_store: Instância do Chroma

    Returns:
        Dicionário com estatísticas
    """
    if not vector_store:
        return {"exists": False, "total_documents": 0}

    try:
        # Tenta obter a coleção
        collection = vector_store._collection
        count = collection.count()

        return {
            "exists": True,
            "total_documents": count,
            "persist_directory": get_persist_dir(),
        }
    except Exception as e:
        return {"exists": True, "total_documents": "unknown", "error": str(e)}


def get_loaded_documents(vector_store: Optional[Chroma]) -> List[dict]:
    """
    Retorna a lista de documentos únicos já carregados no vector store.
    Agrupa por arquivo source e retorna informações resumidas.

    Args:
        vector_store: Instância do Chroma

    Returns:
        Lista de dicionários com informações dos documentos:
        [
            {
                "source": "nome_arquivo.md",
                "chunks": 150,
                "type": "markdown",
                "module": "Compras",
                "has_video": True,
                "has_image": False
            },
            ...
        ]
    """
    if not vector_store:
        return []

    try:
        # Obtém todos os documentos da coleção
        collection = vector_store._collection
        result = collection.get(include=["metadatas"])
        
        if not result or not result.get("metadatas"):
            return []
        
        metadatas = result["metadatas"]
        
        # Agrupa por source (nome do arquivo)
        documents_dict = {}
        
        for metadata in metadatas:
            source = metadata.get("source", "unknown")
            
            if source not in documents_dict:
                documents_dict[source] = {
                    "source": source,
                    "chunks": 0,
                    "type": metadata.get("type", "unknown"),
                    "module": metadata.get("module", "N/A"),
                    "has_video": False,
                    "has_image": False,
                    "has_timestamps": False,
                    "youtube_url": metadata.get("youtube_url", None),
                }
            
            # Incrementa contador de chunks
            documents_dict[source]["chunks"] += 1
            
            # Atualiza flags se ainda não foram setadas
            if not documents_dict[source]["has_video"]:
                documents_dict[source]["has_video"] = metadata.get("has_video", False) or bool(metadata.get("videos"))
            
            if not documents_dict[source]["has_image"]:
                documents_dict[source]["has_image"] = metadata.get("has_image", False) or bool(metadata.get("images"))
            
            if not documents_dict[source]["has_timestamps"]:
                documents_dict[source]["has_timestamps"] = metadata.get("has_timestamps") == "true"
        
        # Converte para lista e ordena por nome
        documents_list = sorted(documents_dict.values(), key=lambda x: x["source"])
        
        return documents_list
        
    except Exception as e:
        print(f"❌ Erro ao listar documentos: {e}")
        return []


def check_document_exists(vector_store: Optional[Chroma], filename: str) -> bool:
    """
    Verifica se um documento com o nome dado já existe no vector store.

    Args:
        vector_store: Instância do Chroma
        filename: Nome do arquivo a verificar

    Returns:
        True se o documento já existe, False caso contrário
    """
    if not vector_store:
        return False

    try:
        loaded_docs = get_loaded_documents(vector_store)
        return any(doc["source"] == filename for doc in loaded_docs)
    except Exception:
        return False

