import streamlit as st

# Configuração da Página para visualização Mobile
st.set_page_config(page_title="Bizuário PP - PRF", layout="centered")

st.title("🛡️ Fiscalização de Produtos Perigosos")
st.caption("Versão Digital do Bizuário Técnico - 2026")
st.markdown("---")

# =========================================================
# ETAPA 0: INÍCIO DA ABORDAGEM (CONDUTOR)
# =========================================================
st.header("Etapa 0: Início da Abordagem (Condutor)")

st.subheader("Passo 2.4: O condutor possui o Curso Especializado de Transporte de Produtos Perigosos (CETPP) válido e averbado?")

with st.expander("ℹ️ Ação Recomendada (Clique para ver)", expanded=True):
    st.write("Verifique na CNH Digital ou pelo CPF no aplicativo **'Fiscalização Senatran'**. A informação deve estar na base RENACH.")

# Usando colunas para os botões de decisão
col1, col2 = st.columns(2)
with col1:
    mopp_sim = st.button("✅ SIM (Curso Ativo)")
with col2:
    mopp_nao = st.button("❌ NÃO (Vencido/Inexistente)")

if mopp_nao:
    st.error("🚨 DETALHAMENTO DAS INFRAÇÕES (Em caso de 'NÃO'):")
    
    st.markdown("""
    **1. Esfera de Trânsito (CTB):**
    * **Art. 162, VII:** Dirigir veículo sem possuir os cursos especializados previstos no CTB.
    * **Resumo:** Infração específica para o condutor que não comprova a formação técnica exigida para a carga.

    **2. Esfera de Transporte (Res. 5.998/22 ANTT):**
    * **Art. 43, §2º, XIX ou XX (Transportador):** Transportar produtos perigosos com condutor que não possua curso especializado ou com curso vencido.
    * **Resumo:** Responsabilidade da empresa transportadora por permitir que condutor sem o CETPP realize a viagem.
    * **Art. 43, §6º, XIII ou XXIV (Expedidor):** Expedir produtos perigosos em veículo cujo condutor não possua o curso especializado exigido.
    * **Resumo:** Responsabilidade de quem envia a carga por não conferir a habilitação técnica do motorista no ato do carregamento.
    """)
    
    st.warning("⚖️ **ENQUADRAMENTOS CRIMINAIS (Campo de Observações):**")
    st.markdown("""
    * **Crime Ambiental (Art. 56 da Lei 9.605/98):** Transportar substância tóxica/nociva em desacordo com as exigências. Usar quando a falta do curso configurar grande risco à saúde ou meio ambiente.
    * **Falsificação/Uso de Doc. Falso (Art. 297 e 304 CP):** Usar no caso de condutor apresentar certificado flagrantemente falso ou adulterado.
    """)

st.divider()

# =========================================================
# ETAPA 1: DOCUMENTAÇÃO ESPECÍFICA (CIV E CIPP)
# =========================================================
st.header("Etapa 1: Documentação Específica")

st.info("**Filtro Inicial:** O transporte é realizado **A GRANEL**?")
modalidade = st.radio("Selecione a modalidade:", ["Não (Carga fracionada - Pular para sinalização)", "Sim (Exigir CIV e CIPP)"])

if "Sim" in modalidade:
    # --- PASSO 5: CIV ---
    st.subheader("Passo 5: Verificação do CIV")
    st.markdown("> **O que é o CIV?** Atesta que o veículo (trator ou rebocado) foi inspecionado pelo INMETRO e está em condições mecânicas (freios, pneus, etc).")
    
    with st.expander("💡 Bizu do CIV"):
        st.write("Se for uma carreta, deve haver um CIV para o Cavalo-Trator e outro para o Semirreboque.")

    c51 = st.checkbox("5.1: Apresentou CIV original (físico/digital) para TODOS os veículos?")
    c52 = st.checkbox("5.2: O CIV está dentro da validade (Geralmente anual)?")
    c53 = st.checkbox("5.3: Placa e Chassi no CIV conferem com o veículo?")

    if not c51 or not c52 or not c53:
        st.error("🚨 INFRAÇÃO (CIV): Art. 43, II, 'f' da Res. 5.998/22 ANTT")
        st.write("**Resumo:** Veículo sem inspeção, vencida ou dados divergentes. **Medida:** Retenção para regularização ou transbordo.")

    st.markdown("---")

    # --- PASSO 6: CIPP ---
    st.subheader("Passo 6: Verificação do CIPP")
    st.markdown("> **O que é o CIPP?** Atesta que o equipamento (tanque/silo) suporta a pressão e a corrosão do produto.")

    c61 = st.checkbox("6.1: Apresentou CIPP original (nome do proprietário conferindo)?")
    c62 = st.checkbox("6.2: CIPP está na validade (6 meses a 3 anos conforme o produto)?")
    c63 = st.checkbox("6.3: Número do equipamento (placa do tanque) confere com o CIPP?")
    c64 = st.checkbox("6.4: Produto na NF é compatível com os autorizados no verso do CIPP?")

    if not c61 or not c62 or not c63:
        st.error("🚨 INFRAÇÃO (CIPP): Art. 43, II, 'f' da Res. 5.998/22 ANTT")
        st.write("**Resumo:** Falta de integridade técnica do recipiente. **Medida:** Retenção.")
    
    if not c64:
        st.error("🚨 INFRAÇÃO (CIPP): Art. 43, II, 'd' da Res. 5.998/22 ANTT")
        st.write("**Resumo:** Tanque NÃO autorizado para este produto específico. **Medida:** Retenção para transbordo.")

st.divider()
st.info("Aguardando as próximas etapas: Documentação de Transporte (Passo 11)...")
