#!/bin/bash
# Script para regenerar a documentação com as melhorias RAG

echo "🚀 Rodando Agente Koper V2"
echo "================================================"
echo ""

# Ativa o ambiente virtual
source venv/bin/activate

# Roda o Streamlit
streamlit run frontend/main.py
