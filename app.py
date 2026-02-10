import streamlit as st

# Configuração da interface
st.set_page_config(page_title="Sistema de Fiscalização PP", layout="centered")

# Controle de fluxo interno
if 'fluxo' not in st.session_state:
    st.session_state.fluxo = 'abertura'

# =========================================================
# PROTOCOLO DE ABERTURA
# =========================================================
if st.session_state.fluxo == 'abertura':
    st.title("🛡️ Supervisão de Transporte de Produtos Perigosos")
    st.markdown("---")
    st.subheader("Diretrizes de Fiscalização Rodoviária")
    
    st.markdown("""
    Prezado agente, 

    Este sistema orienta a fiscalização técnica de veículos destinados ao transporte de produtos perigosos, em estrita observância à **Resolução ANTT nº 5.998/22** e ao **Código de Trânsito Brasileiro**.

    **Escopo do Procedimento:**
    * **Qualificação Profissional:** Validação da CNH (validade e categoria) e regularidade do curso técnico (CETPP).
    * **Inspeção Técnica Veicular:** Validação de certificados CIV e CIPP para granéis.
    * **Controle Documental:** Análise de Notas Fiscais, Declarações do Expedidor e enquadramentos de quantidade.
    * **Segurança Operacional:** Conferência de EPIs, Conjuntos de Emergência e Sinalização Externa.
    * **Conclusão e Enquadramentos:** Relatório consolidado de infrações e medidas administrativas.
    """)
    
    if st.button("🚀 Iniciar Procedimento Fiscal"):
        st.session_state.fluxo = 'condutor'
        st.rerun()

# =========================================================
# VERIFICAÇÃO DE QUALIFICAÇÃO PROFISSIONAL
# =========================================================
elif st.session_state.fluxo == 'condutor':
    st.header("Identificação e Regularidade do Condutor")
    
    # 1. VALIDADE DA CNH
    st.subheader("Validação Cronológica do Documento de Habilitação")
    cnh_validade = st.radio("A Carteira Nacional de Habilitação (CNH) encontra-se dentro do prazo de validade?", 
                            ["Em análise", "Sim (Documento válido)", "Não (Vencida há mais de 30 dias)"])
    
    if cnh_validade == "Não (Vencida há mais de 30 dias)":
        st.error("🚨 Infração Identificada: Art. 162, V do CTB (Dirigir veículo com validade da CNH vencida há mais de 30 dias).")

    st.markdown("---")

    # 2. CATEGORIA DA CNH
    st.subheader("Compatibilidade de Categoria de Habilitação")
    
    with st.expander("📄 Observações Técnicas: Categorias de Habilitação (Resumo)", expanded=False):
        st.markdown("""
        * **Categoria A:** Veículos motorizados de duas ou três rodas.
        * **Categoria B:** Veículos motorizados até 3.500 kg de PBT e até 8 lugares.
        * **Categoria C:** Veículos de carga acima de 3.500 kg de PBT (Caminhão comum).
        * **Categoria D:** Veículos de passageiros com lotação superior a 8 lugares.
        * **Categoria E:** Unidade acoplada (reboque/semirreboque) com 6.000 kg ou mais de PBT.
        """)
        
    cnh_categoria = st.radio("A categoria do condutor é compatível com o conjunto veicular?", 
                             ["Em análise", "Sim (Categoria compatível)", "Não (Categoria incompatível)"])

    if cnh_categoria == "Não (Categoria incompatível)":
        st.error("🚨 Infração Identificada: Art. 162, III do CTB (Categoria diferente da qual está habilitado).")

    st.markdown("---")

    # 3. CURSO TÉCNICO (CETPP/MOPP)
    st.subheader("Verificação do Curso Especializado (CETPP/MOPP)")
    st.info("Consulte a base RENACH via sistema 'Fiscalização Senatran'.")

    status_mopp = st.radio("Status da averbação técnica no sistema:", 
                           ["Em análise", "Regular (Curso ativo e averbado)", "Irregular (Vencido, ausente ou não averbado)"])

    if status_mopp == "Regular (Curso ativo e averbado)":
        st.success("Habilitação técnica confirmada.")
        if st.button("Avançar para Certificações Técnicas ➡️"):
            st.session_state.fluxo = 'documentacao_tecnica'
            st.rerun()

    elif status_mopp == "Irregular (Vencido, ausente ou não averbado)":
        st.error("🚨 Identificação de Irregularidade:")
        st.markdown("**Art. 162, VII do CTB:** Conduzir veículo sem os cursos especializados obrigatórios.")
        
        with st.expander("⚖️ Detalhamento ANTT e Penal", expanded=True):
            st.markdown("""
            **Resolução ANTT 5.998/22:**
            * **Transportador (Art. 43, §2º, XIX/XX):** Permitir condutor sem qualificação.
            * **Expedidor (Art. 43, §6º, XIII/XXIV):** Falha na conferência documental.

            **Enquadramentos Penais:**
            * **Crime Ambiental (Lei 9.605/98, Art. 56):** Transporte em desacordo com as exigências.
            * **Falsidade (Art. 297/304 CP):** Uso de documento falso.
            """)
        
        if st.button("Prosseguir com a Fiscalização ➡️"):
            st.session_state.fluxo = 'documentacao_tecnica'
            st.rerun()

# Espaço para Etapa 1
elif st.session_state.fluxo == 'documentacao_tecnica':
    st.header("Certificações Técnicas (CIV/CIPP)")
    if st.button("⬅️ Retornar"):
        st.session_state.fluxo = 'condutor'
        st.rerun()
    st.write("Aguardando inserção dos dados de CIV e CIPP...")
