import streamlit as st

# Configuração da interface
st.set_page_config(page_title="Fiscalização de PP - NSV/RN", layout="centered")

# Controle de fluxo interno (Navegação sem pular etapas)
if 'fluxo' not in st.session_state:
    st.session_state.fluxo = 'abertura'

# =========================================================
# PROTOCOLO DE ABERTURA - NSV/RN
# =========================================================
if st.session_state.fluxo == 'abertura':
    st.title("🛡️ Fiscalização de Transporte de Produtos Perigosos")
    st.markdown("---")
    
    st.markdown("""
    ### Informativo Institucional
    Este sistema foi desenvolvido pelo **Núcleo de Segurança Viária (NSV) da PRF no Rio Grande do Norte** para servir como ferramenta de suporte à decisão durante a fiscalização de veículos que transportam produtos perigosos.

    **Roteiro da Fiscalização:**
    1. **Qualificação Profissional:** CNH (categoria/validade) e curso específico (CETPP).
    2. **Trajes e Passageiros:** Verificação de vestuário e proibição de caronas.
    3. **Certificações Técnicas:** Inspeção de CIV e CIPP para equipamentos a granel.
    4. **Controle Documental:** Nota Fiscal, Declaração do Expedidor e isenções.
    5. **Segurança e Sinalização:** EPIs, Conjunto de Emergência e identificação da carga.
    """)
    
    if st.button("🚀 Iniciar Procedimento de Fiscalização"):
        st.session_state.fluxo = 'condutor'
        st.rerun()

# =========================================================
# 1. IDENTIFICAÇÃO E REGULARIDADE DO CONDUTOR
# =========================================================
elif st.session_state.fluxo == 'condutor':
    st.header("Qualificação Profissional do Condutor")
    
    # 1.1 VALIDADE DA CNH
    st.subheader("Validação Cronológica da CNH")
    cnh_validade = st.radio("A CNH encontra-se dentro do prazo de validade?", 
                            ["Em análise", "Sim (Documento válido)", "Não (Vencida há mais de 30 dias)"])
    if cnh_validade == "Não (Vencida há mais de 30 dias)":
        st.error("🚨 Infração Identificada: Art. 162, V do CTB.")

    st.markdown("---")

    # 1.2 CATEGORIA DA CNH
    st.subheader("Compatibilidade de Categoria")
    with st.expander("📄 Tabela de Categorias (Resumo)", expanded=False):
        st.markdown("""
        * **Cat. A:** 2 ou 3 rodas.
        * **Cat. B:** Até 3.500 kg PBT / 8 passageiros.
        * **Cat. C:** Carga acima de 3.500 kg PBT.
        * **Cat. D:** Passageiros acima de 8 lugares.
        * **Cat. E:** Unidade acoplada com 6.000 kg ou mais de PBT.
        """)
    cnh_categoria = st.radio("A categoria é compatível com o conjunto?", 
                             ["Em análise", "Sim (Compatível)", "Não (Incompatível)"])
    if cnh_categoria == "Não (Incompatível)":
        st.error("🚨 Infração Identificada: Art. 162, III do CTB.")

    st.markdown("---")

    # 1.3 CURSO TÉCNICO (CETPP)
    st.subheader("Curso Especializado (CETPP)")
    with st.expander("ℹ️ Resumo Técnico (Base Legal)", expanded=True):
        st.markdown("""
        O CETPP é obrigatório (Art. 145 CTB, Res. 1020/25 CONTRAN). 
        * **Nota:** Para autuação, utiliza-se o termo **'especializado'**.
        * **Consulta:** CNH Digital ou RENACH (Fiscalização Senatran).
        """)

    status_mopp = st.radio("O curso técnico consta como ativo e averbado?", 
                           ["Em análise", "Sim (Curso Regular)", "Não (Ausente/Vencido/Não averbado)"])

    if status_mopp == "Sim (Curso Regular)":
        st.success("Habilitação técnica confirmada.")
        if st.button("Avançar para Trajes e Caronas ➡️"):
            st.session_state.fluxo = 'trajes_caronas'
            st.rerun()
    elif status_mopp == "Não (Ausente/Vencido/Não averbado)":
        st.error("🚨 Irregularidade Identificada:")
        st.markdown("""
        **Esfera de Trânsito:** Art. 162, VII do CTB.
        **Esfera de Transporte (ANTT):** Transportador (Art. 43, §2º, XIX/XX) e Expedidor (Art. 43, §6º, XIII/XXIV).
        """)
        with st.warning("⚖️ Enquadramentos Penais"):
            st.markdown("* **Crime Ambiental:** Art. 56, Lei 9.605/98.\n* **Falsidade:** Art. 297/304 CP.")
        
        if st.button("Prosseguir com a Fiscalização ➡️"):
            st.session_state.fluxo = 'trajes_caronas'
            st.rerun()

# =========================================================
# 2. TRAJES E CARONAS (ART. 22 E ART. 17 RTRPP)
# =========================================================
elif st.session_state.fluxo == 'trajes_caronas':
    st.header("Verificação de Trajes e Passageiros")
    
    if st.button("⬅️ Voltar"):
        st.session_state.fluxo = 'condutor'
        st.rerun()

    st.markdown("---")

    # 2.1 TRAJES (Art. 22 RTRPP)
    st.subheader("Vestuário do Condutor e Auxiliares")
    with st.expander("📄 Requisito Legal", expanded=True):
        st.write("Obrigatório: Calça comprida, camisa/camiseta e calçados fechados.")

    traje_ok = st.radio("Estão adequadamente trajados?", ["Em análise", "Sim", "Não"])
    if traje_ok == "Não":
        st.error("🚨 Infração (ANTT): Art. 43, §4º, X (Transportador).")
        st.warning("⚠️ Medida Administrativa: Regularização imediata para prosseguir.")

    st.markdown("---")

    # 2.2 CARONAS (Art. 17, I RTRPP)
    st.subheader("Presença de Passageiros")
    caronas = st.radio("Há presença de caronas (não auxiliares)?", ["Em análise", "Não", "Sim"])
    if caronas == "Sim":
        st.error("🚨 Infração (ANTT): Art. 43, §3º, XII (Transportador).")
        st.warning("⚠️ Ação: Retirada imediata dos passageiros.")

    if st.button("Avançar para Certificações Técnicas ➡️"):
        st.session_state.fluxo = 'documentacao_tecnica'
        st.rerun()

# =========================================================
# 3. CERTIFICAÇÕES TÉCNICAS (PRÓXIMA FASE)
# =========================================================
elif st.session_state.fluxo == 'documentacao_tecnica':
    st.header("Certificações Técnicas (CIV e CIPP)")
    if st.button("⬅️ Retornar"):
        st.session_state.fluxo = 'trajes_caronas'
        st.rerun()
    st.write("Seção em desenvolvimento...")
