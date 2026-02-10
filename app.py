import streamlit as st

st.set_page_config(page_title="Bizuário PRF - PP", layout="wide")

# --- ETAPA 0: INÍCIO DA ABORDAGEM (CONDUTOR) ---
st.title("🛡️ Fiscalização de Produtos Perigosos")
st.header("Etapa 0: Início da Abordagem (Condutor)")

st.subheader("Passo 2.4: O condutor possui o Curso Especializado de Transporte de Produtos Perigosos (CETPP) válido e averbado?")
st.info("**Ação Recomendada:** Verifique na CNH Digital ou pelo CPF no aplicativo 'Fiscalização Senatran'. A informação deve estar na base RENACH.")

mopp = st.radio("Resultado da consulta:", ("Sim (Curso ativo no sistema)", "Não (Curso vencido, inexistente ou não averbado)"))

if "Não" in mopp:
    st.error("🚨 DETALHAMENTO DAS INFRAÇÕES (Em caso de 'NÃO'):")
    st.markdown("""
    **1. Esfera de Trânsito (CTB):**
    * **Art. 162, VII:** Dirigir veículo sem possuir os cursos especializados previstos no CTB.
    * **Resumo:** Infração específica para o condutor que não comprova a formação técnica exigida para a carga.

    **2. Esfera de Transporte (Res. 5.998/22 ANTT):**
    * **Art. 43, §2º, XIX ou XX (Transportador):** Transportar produtos perigosos com condutor sem o curso especializado ou com o curso vencido.
    """)

st.divider()

# --- ETAPA 1: DOCUMENTAÇÃO ESPECÍFICA ---
st.header("Etapa 1: Documentação Específica")

# Filtro Inicial
modalidade = st.radio("O transporte é realizado A GRANEL?", ("Sim (Exigir CIV e CIPP)", "Não (Carga fracionada - Pular para Próximo Passo)"))

if "Sim" in modalidade:
    # --- PASSO 5: CIV ---
    st.subheader("Passo 5: Verificação do CIV (Certificado de Inspeção Veicular)")
    st.write("**O que é?** Atesta que o veículo (trator ou rebocado) está em condições mecânicas e de segurança (pneus, freios, luzes).")
    
    civ_status = st.radio("O veículo possui CIV válido?", ("Sim", "Não"))
    if civ_status == "Não":
        st.error("🚨 INFRAÇÃO: Art. 43, II, 'f' da Res. 5.998/22 ANTT.")
        st.write("**Resumo:** Transportar PP em veículo sem certificado de inspeção ou vencido.")

    st.divider()

    # --- PASSO 6: CIPP ---
    st.subheader("Passo 6: Verificação do CIPP")
    st.write("**O que é?** Atesta a integridade do equipamento (tanque/vaso) para suportar pressão e corrosão.")

    c61 = st.radio("6.1: O condutor apresentou o CIPP original (físico ou digital)?", ("Sim", "Não"))
    if c61 == "Não":
        st.error("🚨 INFRAÇÃO: Art. 43, II, 'f' da Res. 5.998/22 ANTT.")
        st.write("**Resumo:** Falta de comprovação da integridade técnica do recipiente que contém a carga perigosa.")

    c62 = st.radio("6.2: O CIPP está dentro do prazo de validade?", ("Sim", "Não"))
    if c62 == "Não":
        st.error("🚨 INFRAÇÃO: Art. 43, II, 'f' da Res. 5.998/22 ANTT.")
        st.write("**Resumo:** O equipamento está com sua inspeção de segurança expirada, oferecendo risco de vazamento ou ruptura.")

    c63 = st.radio("6.3: O número do equipamento confere com o número constante no CIPP?", ("Sim", "Não"))
    if c63 == "Não":
        st.error("🚨 INFRAÇÃO: Art. 43, II, 'f' da Res. 5.998/22 ANTT (CIPP não correspondente).")

    c64 = st.radio("6.4: O produto transportado é compatível com os autorizados no verso do CIPP?", ("Sim", "Não"))
    if c64 == "Não":
        st.error("🚨 INFRAÇÃO: Art. 43, II, 'd' da Res. 5.998/22 ANTT.")
        st.write("**Resumo:** O tanque não foi projetado ou testado para a reatividade ou pressão daquele produto específico.")

st.divider()
st.write("🔄 Aguardando próximos passos do Bizuário...")
