import streamlit as st

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Passo a Passo - Fiscalização PP", layout="centered")

st.title("🚓 Guia de Fiscalização de Produtos Perigosos")
st.write("Siga os passos abaixo na ordem da abordagem.")

# Inicialização das infrações
if 'lista_multas' not in st.session_state:
    st.session_state.lista_multas = []

# --- ETAPA 1: CONDUTOR ---
st.header("1. Verificação do Condutor")
st.info("Instrução: Solicite a CNH e verifique no sistema se o condutor possui o curso MOPP atualizado. Verifique também se ele utiliza calça comprida, camisa e calçado fechado.")

mopp = st.radio("O condutor possui MOPP e traje adequado?", ("Sim", "Não"), index=0, key="c1")
if mopp == "Não":
    if "Infração: Condutor sem curso MOPP ou traje inadequado (Art. 43, II, 'a'/'b' Res. 5998/22)" not in st.session_state.lista_multas:
        st.session_state.lista_multas.append("Infração: Condutor sem curso MOPP ou traje inadequado (Art. 43, II, 'a'/'b' Res. 5998/22)")

st.divider()

# --- ETAPA 2: EQUIPAMENTO ---
st.header("2. Cronotacógrafo e Jornada")
st.info("Instrução: Verifique o certificado de aferição do cronotacógrafo e analise o disco/fita. O motorista deve respeitar 5h30 de direção por 30min de descanso.")

taco = st.radio("Tacógrafo aferido e jornada respeitada?", ("Sim", "Não"), index=0, key="c2")
if taco == "Não":
    if "Infração: Tacógrafo irregular ou Excesso de Jornada (Art. 230, X ou XXIII do CTB)" not in st.session_state.lista_multas:
        st.session_state.lista_multas.append("Infração: Tacógrafo irregular ou Excesso de Jornada (Art. 230, X ou XXIII do CTB)")

st.divider()

# --- ETAPA 3: DOCUMENTOS TÉCNICOS ---
st.header("3. CIV e CIPP")
st.info("Instrução: Peça os certificados de inspeção do veículo (CIV) e do equipamento (CIPP). Verifique se as datas de validade estão em dia.")

docs = st.radio("CIV e CIPP estão presentes e na validade?", ("Sim", "Não"), index=0, key="c3")
if docs == "Não":
    if "Infração: Documentos técnicos vencidos ou inexistentes (Art. 43, II, 'f' Res. 5998/22)" not in st.session_state.lista_multas:
        st.session_state.lista_multas.append("Infração: Documentos técnicos vencidos ou inexistentes (Art. 43, II, 'f' Res. 5998/22)")

st.divider()

# --- ETAPA 4: SINALIZAÇÃO E CARGA ---
st.header("4. Visual do Veículo e NF")
st.info("Instrução: Confira se os painéis laranjas e rótulos de risco correspondem ao produto na Nota Fiscal. Verifique se há vazamentos visíveis.")

carga = st.radio("Sinalização correta e carga sem vazamentos?", ("Sim", "Não"), index=0, key="c4")
if carga == "Não":
    if "Infração: Sinalização irregular ou vazamento (Art. 43, I ou II, 'g' Res. 5998/22)" not in st.session_state.lista_multas:
        st.session_state.lista_multas.append("Infração: Sinalização irregular ou vazamento (Art. 43, I ou II, 'g' Res. 5998/22)")

st.divider()

# --- RESULTADO FINAL ---
st.header("🏁 Resultado da Fiscalização")

if st.button("GERAR RELATÓRIO DE INFRAÇÕES"):
    if st.session_state.lista_multas:
        st.error("🚨 Irregularidades encontradas:")
        for multa in st.session_state.lista_multas:
            st.write(multa)
        st.info("Sugestão: Copie os enquadramentos acima para o seu sistema de multas.")
    else:
        st.success("✅ Nenhuma irregularidade detectada. Veículo liberado!")

if st.button("Limpar e Nova Abordagem"):
    st.session_state.lista_multas = []
    st.rerun()
