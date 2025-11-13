#!/bin/bash
# Script para regenerar a documentação com as melhorias RAG

echo "🚀 Regenerando Documentação Otimizada para RAG"
echo "================================================"
echo ""

# Ativa o ambiente virtual
source venv/bin/activate

# Backup dos documentos antigos
if [ -d "docs" ]; then
    echo "📦 Fazendo backup dos documentos antigos..."
    timestamp=$(date +%Y%m%d_%H%M%S)
    mkdir -p "docs_backup"
    cp -r docs "docs_backup/docs_$timestamp"
    echo "✅ Backup salvo em: docs_backup/docs_$timestamp"
    echo ""
fi

# Remove documentos antigos
echo "🗑️  Removendo documentos antigos..."
rm -rf docs/*.md
echo "✅ Documentos antigos removidos"
echo ""

# Gera nova documentação
echo "📝 Gerando nova documentação otimizada..."
python gerar_documentacao_video.py

echo ""
echo "================================================"
echo "✅ Processo concluído!"
echo ""
echo "📊 Próximos passos:"
echo "1. Verifique os novos documentos em docs/"
echo "2. Reprocesse o vector store no Streamlit"
echo "3. Teste com perguntas variadas"
echo ""
