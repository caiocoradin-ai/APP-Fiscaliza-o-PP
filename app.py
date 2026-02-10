import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Bizuário PRF - PP", layout="centered")

st.title("🛡️ Fiscalização de Produtos Perigosos")
st.markdown("---")

# --- PASSO 1 E 2: CONDUTOR ---
st.header("Etapa 1: Condutor e CETPP")
cpf = st.text_input("CPF do Condutor:")
mopp = st.radio("O condutor possui CETPP (MOPP) ativo?", ("Sim", "Não"))

if mopp == "Não":
    st.error("🚨 INFRAÇÃO DETECTADA")
    st.markdown("""
    **Enquadramento:**
    * **Trânsito:** Art. 162, VII do CTB (Conduzir veículo sem curso especializado).
    * **ANTT:** Art. 43, §2º, XIX/XX (Transportador) e §6º, XIII/XXIV (Expedidor).
    * **Resumo:** A falta do curso impede o condutor de operar carga de risco, gerando responsabilidade também para quem contratou e quem carregou.
    * **Alerta:** Avaliar Crime Ambiental (Art. 56 da Lei 9.605/98) se houver risco iminente.
    """)

st.divider()

# --- PASSO 4: CRONOTACÓGRAFO ---
st.header("Etapa 2: Cronotacógrafo")
pbt = st.number_input("Informe o PBT do veículo (kg):", value=0)

if pbt > 4536:
    st.info("📌 Veículo OBRIGADO a uso de Cronotacógrafo.")
    st.markdown("[🔗 CLIQUE AQUI PARA VERIFICAR AFERIÇÃO NO INMETRO](https://cronotacografo.rbmlq.gov.br/certificados/consultar)")
    
    taco_ok = st.radio("O certificado está válido e o aparelho funcionando?", ("Sim", "Não"))
    if taco_ok == "Não":
        st.error("🚨 INFRAÇÃO: Art. 230, X do CTB")
        st.markdown("**Resumo:** Equipamento obrigatório ineficiente ou inoperante (Aferição vencida ou falta de dados).")
else:
    st.success("✅ Veículo DISPENSADO de Cronotacógrafo (PBT ≤ 4.536kg).")

st.divider()

# --- PASSO 5: FILTROS DE INTELIGÊNCIA ---
st.header("Etapa 3: Inteligência de Carga")
modalidade = st.selectbox("Forma de Transporte:", ["Selecione", "A Granel", "Fracionado"])

if modalidade != "Selecione":
    # Inteligência de Isenção (Tabela Simplificada)
    onu = st.text_input("Digite o Número ONU (ex: 1203):")
    qtd = st.number_input("Quantidade Total na NF (kg ou L):", value=0)
    
    # Base de dados para teste (Gasolina, Diesel, GLP)
    db_isencao = {"1203": 333, "1202": 1000, "1075": 333}
    
    isento = False
    if onu in db_isencao:
        if qtd <= db_isencao[onu]:
            isento = True
            st.success(f"✅ CARGA EM QUANTIDADE LIMITADA (ISENTA).")
            st.markdown(f"**Bizu:** Para o ONU {onu}, o limite é {db_isencao[onu]}. O transporte dispensa MOPP, CIV, CIPP e Sinalização.")
        else:
            st.warning("⚠️ CARGA PLENA DETECTADA. Todas as exigências são aplicáveis.")

    if not isento and modalidade != "Selecione":
        # --- DOCUMENTAÇÃO TÉCNICA (A GRANEL) ---
        if modalidade == "A Granel":
            st.subheader("Verificação de CIV e CIPP")
            civ = st.radio("CIV (Veículo) está válido e presente?", ("Sim", "Não"))
            if civ == "Não":
                st.error("🚨 INFRAÇÃO: Art. 43, II, 'f' da Res. 5.998/22")
                st.write("**Resumo:** Falta de certificado de inspeção técnica de segurança do veículo.")
            
            cipp = st.radio("CIPP (Equipamento/Tanque) está válido e compatível?", ("Sim", "Não"))
            if cipp == "Não":
                st.error("🚨 INFRAÇÃO: Art. 43, II, 'f' ou 'd' da Res. 5.998/22")
                st.write("**Resumo:** Tanque sem inspeção ou não autorizado para este produto.")

        # --- NOTA FISCAL ---
        st.subheader("Documento Fiscal (NF)")
        nf_dados = st.radio("A NF contém ONU, Nome Apropriado e Classe de Risco?", ("Sim", "Não"))
        if nf_dados == "Não":
            st.error("🚨 INFRAÇÃO: Art. 43, III, 'b' da Res. 5.998/22")
            st.write("**Resumo:** Omissão de dados técnicos obrigatórios na Nota Fiscal.")

        declara = st.radio("Possui a 'Declaração do Expedidor' na NF?", ("Sim", "Não"))
        if declara == "Não":
            st.error("🚨 INFRAÇÃO: Art. 43, III, 'a' da Res. 5.998/22")
            st.write("**Resumo:** Falta de atestado de responsabilidade do expedidor sobre o acondicionamento.")

st.markdown("---")
st.caption("Bizuário PRF - Versão de Teste Completa")
