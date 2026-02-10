import streamlit as st

st.set_page_config(page_title="Bizuário PP - PRF", layout="centered")

# Inicialização de estados para não pular etapas
if 'etapa' not in st.session_state:
    st.session_state.etapa = 0

st.title("🛡️ Fiscalização de Produtos Perigosos")
st.caption("Versão Digital do Bizuário Técnico - 2026")
st.markdown("---")

# =========================================================
# ETAPA 0: CONDUTOR
# =========================================================
if st.session_state.etapa == 0:
    st.header("Etapa 0: Início da Abordagem (Condutor)")
    st.subheader("Passo 2.4: O condutor possui o Curso (CETPP) válido?")
    
    with st.expander("ℹ️ Ação Recomendada", expanded=True):
        st.write("Verifique na CNH Digital ou pelo CPF no 'Fiscalização Senatran'.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ SIM (Curso Ativo)"):
            st.session_state.etapa = 1
            st.rerun()
    with col2:
        if st.button("❌ NÃO (Vencido/Inexistente)"):
            st.error("🚨 INFRAÇÕES: Art. 162, VII CTB / Art. 43 ANTT (Transportador e Expedidor).")
            st.warning("⚖️ ALERTA: Avaliar Art. 56 Lei 9.605/98 (Crime Ambiental).")

# =========================================================
# ETAPA 1: DOCUMENTAÇÃO (CIV / CIPP)
# =========================================================
if st.session_state.etapa == 1:
    st.header("Etapa 1: Documentação Específica")
    
    if st.button("⬅️ Voltar ao Condutor"):
        st.session_state.etapa = 0
        st.rerun()

    modalidade = st.radio("O transporte é realizado **A GRANEL**?", 
                          ["Selecione", "Sim (Exigir CIV/CIPP)", "Não (Fracionada)"])

    if modalidade == "Sim (Exigir CIV/CIPP)":
        st.subheader("Passo 5: Verificação do CIV")
        c5 = st.checkbox("CIV presente, válido e condizente com o veículo?")
        
        st.subheader("Passo 6: Verificação do CIPP")
        c6 = st.checkbox("CIPP presente, válido e compatível com o produto?")
        
        if c5 and c6:
            if st.button("Próxima Etapa: Nota Fiscal ➡️"):
                st.session_state.etapa = 2
                st.rerun()
        else:
            st.info("Preencha os requisitos do CIV/CIPP para prosseguir.")
            
    elif modalidade == "Não (Fracionada)":
        if st.button("Próxima Etapa: Nota Fiscal ➡️"):
            st.session_state.etapa = 2
            st.rerun()

# =========================================================
# ETAPA 2: NOTA FISCAL (PASSO 11)
# =========================================================
if st.session_state.etapa == 2:
    st.header("Etapa 2: Documentação de Transporte")
    
    if st.button("⬅️ Voltar para CIV/CIPP"):
        st.session_state.etapa = 1
        st.rerun()

    st.subheader("Passo 11: Verificação da Nota Fiscal")
    # Aqui continuaremos o seu Bizuário da NF...
    st.write("Pronto para configurar os detalhes da NF e Declaração do Expedidor?")
