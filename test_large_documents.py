#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de teste para validar processamento de documentos grandes
"""

import os
import sys
from pathlib import Path

# Adiciona o diretório do projeto ao path
sys.path.insert(0, str(Path(__file__).parent))

from backend.processing import process_markdown_file, count_tokens
import io


def test_large_document():
    """Testa o processamento de um documento grande"""
    
    print("🧪 Teste de Processamento de Documentos Grandes")
    print("=" * 70)
    
    # Caminho para o documento problemático
    doc_path = "docs/Passo a passo - Módulo de Compras_documentacao_gerada.md"
    
    if not os.path.exists(doc_path):
        print(f"❌ Arquivo não encontrado: {doc_path}")
        print("\n💡 Teste com documento de exemplo grande...")
        
        # Cria um documento grande de teste
        test_content = """# Documentação de Teste

## Seção 1

""" + ("Este é um parágrafo de teste. " * 1000 + "\n\n") * 100
        
        # Cria um objeto file-like
        file_like = io.BytesIO(test_content.encode('utf-8'))
        file_like.name = "teste_grande.md"
        
        print(f"📄 Documento de teste criado")
        print(f"📊 Tamanho: {len(test_content):,} caracteres")
        print(f"📊 Estimativa: ~{len(test_content) // 4:,} tokens")
        
    else:
        print(f"📄 Processando: {doc_path}")
        
        # Lê o arquivo real
        with open(doc_path, 'rb') as f:
            content = f.read()
        
        file_like = io.BytesIO(content)
        file_like.name = os.path.basename(doc_path)
        
        print(f"📊 Tamanho: {len(content):,} bytes")
        
    print("\n🔄 Iniciando processamento...")
    print("-" * 70)
    
    try:
        # Processa o arquivo
        chunks = process_markdown_file(file_like)
        
        print("-" * 70)
        print(f"\n✅ SUCESSO!")
        print(f"📦 Total de chunks gerados: {len(chunks)}")
        
        # Estatísticas
        if chunks:
            avg_size = sum(len(c.page_content) for c in chunks) // len(chunks)
            print(f"📏 Tamanho médio por chunk: {avg_size:,} caracteres")
            
            # Verifica metadados
            has_parts = any('part' in c.metadata for c in chunks)
            if has_parts:
                parts = set(c.metadata.get('part', 0) for c in chunks if 'part' in c.metadata)
                print(f"📑 Documento dividido em {len(parts)} partes")
            
            print(f"\n📋 Exemplo de metadados do primeiro chunk:")
            print(f"   {chunks[0].metadata}")
            
            print(f"\n📝 Primeiros 200 caracteres do primeiro chunk:")
            print(f"   {chunks[0].page_content[:200]}...")
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERRO: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    print("\n")
    success = test_large_document()
    print("\n" + "=" * 70)
    
    if success:
        print("🎉 Teste concluído com sucesso!")
        print("\n💡 Próximos passos:")
        print("   1. Execute a aplicação Streamlit: streamlit run frontend/main.py")
        print("   2. Faça upload do documento grande")
        print("   3. O sistema processará automaticamente em partes")
    else:
        print("⚠️  Teste falhou. Verifique os erros acima.")
    
    print("=" * 70)
    print()
