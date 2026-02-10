import streamlit as st

# Configuração da interface
st.set_page_config(page_title="Fiscalização de PP - NSV/RN", layout="centered")

# Controle de fluxo interno
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

    Prezado colega, o objetivo deste guia é otimizar o seu tempo de pista, garantindo que todos os requisitos da **Resolução ANTT nº 5.998/22** e do **CTB** sejam conferidos com precisão técnica e segurança jurídica.

    **Roteiro da Fiscalização:**
    * **Qualificação Profissional:** Validação de CNH (categoria/validade) e curso específico (CETPP).
    * **Certificações Técnicas:** Inspeção de CIV e CIPP para equipamentos a granel.
    * **Controle Documental:** Conferência de Nota Fiscal, Declaração do Expedidor e limites de isenção.
    * **Segurança e Sinalização:** Verificação de EPIs, Conjunto de Emergência e identificação visual da carga.
    * **Desfecho Fiscal:** Relatório consolidado com enquadramentos administrativos e criminais.
    """)
    
    if st.button("🚀 Iniciar Procedimento de Fiscalização"):
        st.session_state.fluxo = 'condutor'
        st.rerun()

# =========================================================
# IDENTIFICAÇÃO E REGULARIDADE DO CONDUTOR
# =========================================================
elif st.session_state.fluxo == 'condutor':
    st.header("Qualificação Profissional do Condutor")
    
    # 1. VALIDADE DA CNH
    st.subheader("Validação Cronológica da CNH")
    cnh_validade = st.radio("O documento de habilitação encontra-se dentro do prazo de validade?", 
                            ["Em análise", "Sim (Documento válido)", "Não (Vencida há mais de 30 dias)"])
    
    if cnh_validade == "Não (Vencida há mais de 30 dias)":
        st.error("🚨 Infração Identificada: Art. 162, V do CTB (Conduzir veículo com CNH vencida há mais de 30 dias).")

    st.markdown("---")

    # 2. CATEGORIA DA CNH
    st.subheader("Compatibilidade de Categoria")
    with st.expander("📄 Tabela de Categorias (Consulta Rápida)", expanded=False):
        st.markdown("""
        * **Cat. A:** Veículos de 2 ou 3 rodas.
        * **Cat. B:** Veículos até 3.500 kg PBT e 8 passageiros.
        * **Cat. C:** Veículos de carga acima de 3.500 kg PBT.
        * **Cat. D:** Transporte de passageiros (acima de 8 lugares).
        * **Cat. E:** Unidade tratora B, C ou D + Unidade acoplada com 6.000 kg ou mais de PBT.
        """)
    cnh_categoria = st.radio("A categoria do condutor é compatível com o conjunto veicular?", 
                             ["Em análise", "Sim (Compatível)", "Não (Incompatível)"])

    if cnh_categoria == "Não (Incompatível)":
        st.error("🚨 Infração Identificada: Art. 162, III do CTB (Categoria divergente da exigida para o veículo).")

    st.markdown("---")

    # 3. CURSO TÉCNICO (CETPP)
    st.subheader("Curso Especializado (CETPP)")
    
    with st.expander("ℹ️ Resumo Técnico sobre o Curso", expanded=True):
        st.markdown("""
        **Base Legal:** O Curso Especializado de Transporte de Produtos Perigosos (CETPP) é requisito indispensável conforme Art. 145 do CTB, Res. 1020/25 CONTRAN e Art. 20 do RTRPP.
        
        **Nota Técnica:** Embora a resolução denomine como curso 'específico', para efeitos de autuação de trânsito, utiliza-se o termo **'especializado'**.
        * Comprovação: CNH Digital ou consulta direta ao **RENACH** via 'Fiscalização Senatran'.
        """)

    status_mopp = st.radio("O curso técnico consta como ativo e averbado no prontuário do condutor?", 
                           ["Em análise", "Sim (Curso Regular)", "Não (Ausente / Vencido / Não averbado)"])

    if status_mopp == "Sim (Curso Regular)":
        st.success("Habilitação técnica confirmada conforme exigência legal.")
        if st.button("Avançar para Certificações Técnicas ➡️"):
            st.session_state.fluxo = 'documentacao_tecnica'
            st.rerun()

    elif status_mopp == "Não (Ausente / Vencido / Não averbado)":
        st.error("🚨 Irregularidade na Qualificação Técnica:")
        
        st.markdown("### Enquadramentos Aplicáveis:")
        st.markdown("""
        **1. Esfera de Trânsito (CTB):**
        * **Art. 162, VII:** Conduzir veículo sem os cursos especializados previstos no CTB. (Infração Gravíssima).
        
        **2. Esfera de Transporte (Res. ANTT 5.998/22):**
        * **Transportador (Art. 43, §2º, XIX/XX):** Permitir a realização do transporte por condutor sem curso especializado válido.
        * **Expedidor (Art. 43, §6º, XIII/XXIV):** Expedir produtos perigosos sem conferir a habilitação técnica do condutor.
        """)

        with st.warning("⚖️ Situações Especiais (Enquadramentos Penais)"):
            st.markdown("""
            * **Crime Ambiental (Art. 56, Lei 9.605/98):** Aplicável se a falta de curso, somada às condições da carga, configurar situação de risco à saúde ou meio ambiente.
            * **Falsidade Documental (Art. 297/304 CP):** Aplicável se houver apresentação de certificado com indícios de contrafação.
            """)
        
        if st.button("Prosseguir com a Fiscalização do Veículo ➡️"):
            st.session_state.fluxo = 'documentacao_tecnica'
            st.rerun()

# Espaço reservado para CIV/CIPP
elif st.session_state.fluxo == 'documentacao_tecnica':
    st.header("Certificações Técnicas (CIV e CIPP)")
    if st.button("⬅️ Retornar ao Condutor"):
        st.session_state.fluxo = 'condutor'
        st.rerun()
    st.write("Análise técnica de veículos e tanques (A Granel) em processamento...")
