import streamlit as st

# --- Configuração da página ---
st.set_page_config(
    page_title="Listagem de EPIs",
    page_icon="⚙️",
    layout="wide"
)

# --- Estilos customizados (CSS) ---
st.markdown("""
    <style>
        /* Remove padding padrão */
        .main {
            padding: 0rem 0rem;
        }

        /* Barra lateral */
        [data-testid="stSidebar"] {
            background-color: #fff;
            border-right: 1px solid #eee;
        }

        [data-testid="stSidebar"] .css-1d391kg, [data-testid="stSidebar"] .css-1v0mbdj {
            padding-top: 1rem;
        }

        /* Aumenta o tamanho do logo */
        [data-testid="stSidebar"] .stImage img {
            width: calc(100% + 2rem);
            margin-left: -1rem;
        }

        /* Estilo para o menu de rádio */
        div[role="radiogroup"] label {
            font-size: 24px !important; /* Tamanho da fonte aumentado */
            margin-bottom: 10px !important; /* Espaçamento entre os itens */
        }

        /* Botões da sidebar */
        .sidebar-item {
            font-size: 16px;
            font-weight: 500;
            color: #333;
            padding: 0.5rem 1rem;
            border-radius: 6px;
            cursor: pointer;
        }

        .sidebar-item:hover {
            background-color: #ffe6cc;
        }

        .sidebar-selected {
            background-color: #ff8b26;
            color: white !important;
        }

        /* Conteúdo central */
        .center-content {
            text-align: center;
            margin-top: 6rem;
        }

        .error-title {
            color: #ff8b26;
            font-weight: 500;
            font-size: 18px;
            margin-top: 1rem;
        }

        .error-subtitle {
            color: #666;
            font-size: 15px;
        }

        /* Botão */
        .retry-button {
            background-color: #ff8b26;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 0.5rem 1.5rem;
            font-size: 15px;
            font-weight: 600;
            margin-top: 1.5rem;
            cursor: pointer;
        }

        .retry-button:hover {
            background-color: #e77a1e;
        }
    </style>
""", unsafe_allow_html=True)


# --- Menu lateral ---
st.sidebar.image("frontend/img/logo.png", use_container_width=True)
menu = st.sidebar.radio(
    "",
    ["Armazenamento", "Compras", "Engenharia", "Financeiro", "Qualidade", "RH", "Suprimentos"],
    index=0
)


# --- Conteúdo da página ---
if menu == "Suprimentos":
    st.markdown("""
    <div class="center-content">
        <img src="https://cdn-icons-png.flaticon.com/512/5951/5951448.png" width="150">
        <p class="error-title">Por algum motivo os EPIs não foram carregados</p>
        <p class="error-subtitle">Se esse problema persistir, por favor relate o problema e mencione esta mensagem de erro.</p>
        <button class="retry-button">Tentar novamente</button>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"<h3 style='text-align:center; margin-top:5rem;'>Módulo de {menu}</h3>", unsafe_allow_html=True)
