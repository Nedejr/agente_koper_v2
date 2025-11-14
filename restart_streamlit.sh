#!/bin/bash

# Script para reiniciar o Streamlit com cache limpo
# Uso: ./restart_streamlit.sh

echo "🔄 Reiniciando Streamlit com correção de vídeo duplicado..."
echo ""

# Cores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 1. Procura processos do Streamlit rodando
echo "1️⃣  Verificando processos do Streamlit..."
STREAMLIT_PID=$(pgrep -f "streamlit run")

if [ ! -z "$STREAMLIT_PID" ]; then
    echo -e "${YELLOW}   ⚠️  Streamlit rodando (PID: $STREAMLIT_PID). Parando...${NC}"
    kill $STREAMLIT_PID
    sleep 2
    echo -e "${GREEN}   ✅ Streamlit parado${NC}"
else
    echo -e "${GREEN}   ✅ Nenhum processo Streamlit rodando${NC}"
fi

# 2. Limpa cache do Streamlit
echo ""
echo "2️⃣  Limpando cache do Streamlit..."
if [ -d "$HOME/.streamlit/cache" ]; then
    rm -rf $HOME/.streamlit/cache
    echo -e "${GREEN}   ✅ Cache limpo${NC}"
else
    echo -e "${YELLOW}   ⚠️  Pasta de cache não encontrada (já estava limpa)${NC}"
fi

# 3. Opção de limpar base de dados (comentado por padrão)
echo ""
echo "3️⃣  Verificando base de dados..."
if [ -d "db" ]; then
    echo -e "${YELLOW}   ⚠️  Base de dados existe em ./db/${NC}"
    read -p "   Deseja limpar a base de dados? (s/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Ss]$ ]]; then
        rm -rf db/
        echo -e "${GREEN}   ✅ Base de dados removida. Será necessário recarregar documentos.${NC}"
    else
        echo -e "${YELLOW}   ⏭️  Base mantida (documentos não serão recarregados)${NC}"
    fi
else
    echo -e "${YELLOW}   ⚠️  Pasta db/ não encontrada${NC}"
fi

# 4. Reinicia o Streamlit
echo ""
echo "4️⃣  Iniciando Streamlit..."
echo -e "${GREEN}   🚀 Iniciando em http://localhost:8501${NC}"
echo ""
echo "   Pressione Ctrl+C para parar"
echo ""

# Inicia o Streamlit
streamlit run frontend/main.py
