import streamlit as st

st.set_page_config(page_title="Fiscalização PP - PRF", layout="centered")

st.title("🛡️ Sistema de Fiscalização PP")
st.subheader("Consultoria Técnica de Produtos Perigosos")

# --- ETAPA 0: CONDUTOR ---
st.header("1. Identificação do Condutor")
cpf = st.text_input("CPF do Condutor (Para consulta no Senatran)")
mopp = st.radio("O condutor possui CETPP (MOPP) ativo no sistema?", ("Sim", "Não"))

if mopp == "Não":
    st.error("🚨 INFRAÇÃO DETECTADA")
    st.write("**Enquadramentos:**")
    st.write("- **Trânsito:** Art. 162, VII do CTB (Falta de curso especializado).")
    st.write("- **Transporte (ANTT):** Art. 43, §2º, XIX/XX (Transportador) e §6º, XIII/XXIV (Expedidor).")
    st.warning("⚠️ **ALERTA CRIMINAL:** Avaliar Crime Ambiental (Art. 56 Lei 9.605/98) se houver grande risco.")

st.divider()

# --- ETAPA 0.1: TACÓGRAFO ---
st.header("2. Equipamento Obrigatório")
pbt = st.number_input("Informe o PBT do veículo (kg):", value=0)

if pbt > 4536:
    st.info("📌 Veículo OBRIGADO a uso de Cronotacógrafo.")
    st.markdown("[Clique aqui para consultar aferição no INMETRO](https://cronotacografo.rbmlq.gov.br/certificados/consultar)")
else:
    st.success("✅ Veículo DISPENSADO de Cronotacógrafo.")

st.divider()

# --- ETAPA 1: INTELIGÊNCIA DE CARGA ---
st.header("3. Inteligência de Carga")
modalidade = st.selectbox("Modalidade de Transporte:", ["Selecione", "A Granel", "Fracionado"])

if modalidade != "Selecione":
    onu = st.text_input("Digite o Número ONU (ex: 1203):")
    qtd = st.number_input("Quantidade Total (kg ou L):", value=0)

    # Simulação da base de dados (Exemplos)
    db_isencao = {"1203": 333, "1202": 1000, "1005": 20}

    if onu in db_isencao:
        limite = db_isencao[onu]
        if qtd <= limite:
            st.success(f"✅ CARGA EM QUANTIDADE LIMITADA (Isenta). Limite para ONU {onu} é {limite}kg.")
            st.write("Dispensa: MOPP, CIV, CIPP e Sinalização Externa.")
        else:
            st.warning(f"⚠️ CARGA PLENA. Limite de {limite}kg excedido.")
            
            # Se for Granel, exige CIV e CIPP
            if modalidade == "A Granel":
                st.subheader("Documentação Técnica (A Granel)")
                civ = st.checkbox("CIV Válido e Presente?")
                cipp = st.checkbox("CIPP Válido e Compatível?")
                if not civ or not cipp:
                    st.error("🚨 INFRAÇÃO: Art. 43, II, 'f' da Res. 5.998/22.")

st.divider()
st.info("Próximo passo: Verificação de Sinalização e Estiva...")
