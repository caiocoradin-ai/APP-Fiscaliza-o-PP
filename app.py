import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Bizuário PRF - PP", layout="wide", page_icon="🚓")

# Estilo CSS para melhorar a visualização
st.markdown("""
    <style>
    .stAlert p { font-weight: 600; }
    .main { background-color: #f5f7f9; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DADOS (Dicionário ONU)
@st.cache_data
def carregar_dados():
    try:
        # Tenta carregar o CSV que você criou
        df = pd.read_csv("produtos_onu.csv")
        return df
    except:
        return None

df_onu = carregar_dados()

# Inicialização da Memória (Estado da Sessão)
if 'infrações' not in st.session_state:
    st.session_state.infrações = []
if 'produto_selecionado' not in st.session_state:
    st.session_state.produto_selecionado = None

# 3. TÍTULO E CABEÇALHO
st.title("🚓 Bizuário Digital - Produtos Perigosos")
st.caption("Baseado na Resolução ANTT 5.998/22 e MPO-005")

if df_onu is None:
    st.error("Erro: Arquivo 'produtos_onu.csv' não encontrado no repositório.")
    st.stop()

# --- BARRA LATERAL: BUSCA E ISENÇÃO ---
with st.sidebar:
    st.header("🔍 Identificação")
    busca = st.text_input("Número ONU ou Nome:")
    
    if busca:
        resultado = df_onu[(df_onu['onu'].astype(str).str.contains(busca)) | (df_onu['nome'].str.contains(busca.upper()))]
        if not resultado.empty:
            ops = [f"{row['onu']} - {row['nome']}" for i, row in resultado.iterrows()]
            escolha = st.selectbox("Selecione o produto:", ops)
            idx = int(escolha.split(" - ")[0])
            st.session_state.produto_selecionado = df_onu[df_onu['onu'] == idx].iloc[0]
        else:
            st.error("Produto não encontrado.")

if st.session_state.produto_selecionado is not None:
    prod = st.session_state.produto_selecionado
    st.info(f"**Produto:** {prod['nome']} | **Classe:** {prod['classe']}")
    
    limite = float(prod['limite_coluna8'])
    peso = st.number_input(f"Peso Bruto (kg) - Limite Col. 8 é {limite}kg:", min_value=0.0)
    
    isento = False
    if peso > 0:
        if limite > 0 and peso <= limite:
            st.success("✅ CARGA ISENTA (Quant. Limitada)")
            st.warning("⚠️ Exigir: Extintor 2kg e frase 'QUANTIDADE LIMITADA' na NF.")
            isento = True
        else:
            st.error("🚨 NÃO ISENTO - Fiscalização Completa")

    # --- ABAS DE FISCALIZAÇÃO ---
    aba1, aba2, aba3, aba4, aba5 = st.tabs([
        "👤 Condutor/Equipe", "⏱️ Tacógrafo/Jornada", "📄 Docs Técnicos/NF", "📦 Carga/Segurança", "📝 Relatório Final"
    ])

    with aba1:
        st.subheader("Fiscalização da Equipe")
        if st.checkbox("Condutor sem curso MOPP (verificar sistema)"):
            st.session_state.infrações.append("Sem curso MOPP (Art. 43, II, 'a') - Resp: Transp.")
        if st.checkbox("Condutor/Ajudante com traje inadequado (Bermuda/Chinelo)"):
            st.session_state.infrações.append("Traje inadequado (Art. 43, II, 'b') - Resp: Transp.")
        if st.checkbox("Presença de pessoa não autorizada (Carona)"):
            st.session_state.infrações.append("Pessoa não autorizada (Art. 43, II, 'c') - Resp: Transp.")
        st.info("💡 Lembrete: O traje deve ser calça, camisa e calçado fechado.")

    with aba2:
        st.subheader("Cronotacógrafo e Lei 13.103/15")
        st.link_button("🌐 Consultar Validade INMETRO", "https://cronotacografo.rbmlq.gov.br/outros-servicos/consultar-certificado-provisorio")
        
        c1, c2 = st.columns(2)
        with c1:
            if st.checkbox("Tacógrafo Vencido/Inoperante"):
                st.session_state.infrações.append("Tacógrafo irregular (Art. 230, X CTB)")
            if st.checkbox("Falta de dados no disco (Nome/Data/Placa)"):
                st.session_state.infrações.append("Disco/Fita sem dados (Art. 230, X CTB)")
        with c2:
            st.markdown("**Tempo de Direção/Descanso**")
            if st.checkbox("Excesso de jornada detectado"):
                tem_ppd = st.radio("Há Ponto de Parada (PPD) no trecho?", ["Sim", "Não"], index=1)
                if tem_ppd == "Sim":
                    st.session_state.infrações.append("Excesso jornada/falta descanso (Art. 230, XXIII CTB)")
                else:
                    st.warning("Não autuar por tempo de direção neste trecho (ausência de PPD).")

    with aba3:
        st.subheader("Documentação e Notas")
        if st.checkbox("NF sem Declaração do Expedidor"):
            st.session_state.infrações.append("Falta Declaração do Expedidor (Art. 43, III, 'a') - Resp: Exped.")
        if st.checkbox("Dados do produto na NF incorretos/incompletos"):
            st.session_state.infrações.append("NF com dados incompletos (Art. 43, III, 'b') - Resp: Exped.")
        
        st.divider()
        st.subheader("Certificados Técnicos")
        veiculo_novo = st.toggle("Veículo com menos de 1 ano?")
        if not veiculo_novo:
            if st.checkbox("CIV Vencido ou Inexistente"):
                st.session_state.infrações.append("Sem CIV válido (Art. 43, II, 'f') - Resp: Transp.")
        
        retorno_vazio = st.toggle("Retorno de vazio contaminado?")
        if retorno_vazio:
            st.info("ℹ️ Tolerância de 30 dias para o CIPP após o vencimento.")
        if st.checkbox("CIPP Vencido ou Inexistente"):
            if not (retorno_vazio): # Lógica simplificada
                 st.session_state.infrações.append("Sem CIPP válido (Art. 43, II, 'f') - Resp: Transp.")

    with aba4:
        st.subheader("Segurança, Sinalização e Carga")
        tipo_carga = st.radio("Tipo de Carregamento:", ["Fracionado", "Granel"])
        
        if st.checkbox("Incompatibilidade entre produtos detectada"):
            cofre = st.checkbox("Utiliza Cofre de Carga?")
            if not cofre:
                st.error("Risco de reação química ou contaminação!")
                st.session_state.infrações.append("Carga Incompatível (Art. 43, IV, 'a') - Resp: Exped.")
        
        if st.checkbox("Sinalização (Painel/Rótulo) inexistente ou incorreta"):
            st.session_state.infrações.append("Sinalização Irregular (Art. 43, I, 'a/b') - Resp: Transp/Exped.")
            
        if st.checkbox("Pneus em mau estado (Careca/Bolha)"):
            st.session_state.infrações.append("Pneus em mau estado (Art. 230, XVIII CTB)")
            
        if st.checkbox("Vazamento ou carga mal acondicionada"):
            st.session_state.infrações.append("Vazamento/Acondicionamento irregular (Art. 43, II, 'g')
