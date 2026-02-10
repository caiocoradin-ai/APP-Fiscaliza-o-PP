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
    
    st.write("""
    Este sistema tem por objetivo orientar o agente na fiscalização técnica de veículos destinados ao transporte de produtos perigosos, em estrita observância à **Resolução ANTT nº 5.998/22** e ao **Código de Trânsito Brasileiro**.

    **Abrangência do Procedimento:**
    * **Qualificação Profissional:** Verificação da regularidade do condutor (CETPP).
    * **Inspeção Técnica Veicular:** Validação de certificados CIV e CIPP para granéis.
    * **Controle Documental:** Análise de Notas Fiscais, Declarações do Expedidor e enquadramentos de quantidade.
    * **Segurança Operacional:** Conferência de EPIs, Conjuntos de Emergência e Sinalização Externa.
    * **Conclusão e Enquadramentos:** Relatório consolidado de infrações e medidas administrativas.
    """)
    
    if st.button("Iniciar Procedimento Fiscal"):
        st.session_state.fluxo = 'condutor'
        st.rerun()

# =========================================================
# VERIFICAÇÃO DE QUALIFICAÇÃO PROFISSIONAL
# =========================================================
elif st.session_state.fluxo == 'condutor':
    st.header("Identificação e Regularidade do Condutor")
    
    st.markdown("#### Verificação do Curso Especializado (CETPP/MOPP)")
    
    st.info("**Procedimento:** Consultar a base RENACH via sistema 'Fiscalização Senatran' para confirmar a averbação e validade do curso técnico.")

    status_mopp = st.radio("Status da habilitação técnica:", 
                           ["Em análise", "Regular (Curso ativo e averbado)", "Irregular (Vencido, ausente ou não averbado)"])

    if status_mopp == "Regular (Curso ativo e averbado)":
        st.success("Condutor habilitado para a operação.")
        if st.button("Avançar para Certificações Técnicas ➡️"):
            st.session_state.fluxo = 'documentacao_tecnica'
            st.rerun()

    elif status_mopp == "Irregular (Vencido, ausente ou não averbado)":
        st.error("🚨 Constatação de Irregularidades:")
        
        st.markdown("### Enquadramentos Jurídicos:")
        
        st.markdown("#### Esfera de Trânsito")
        st.write("**Art. 162, VII do CTB:** Conduzir veículo sem os cursos especializados obrigatórios. Infração de natureza gravíssima.")
        
        st.markdown("#### Esfera de Transporte (ANTT)")
        st.markdown("""
        * **Responsabilidade do Transportador (Art. 43, §2º, XIX/XX):** Permitir a realização do transporte por condutor sem a devida qualificação técnica.
        * **Responsabilidade do Expedidor (Art. 43, §6º, XIII/XXIV):** Expedir carga em veículo cujo condutor não comprove a habilitação exigida.
        """)

        st.warning("⚖️ Implicações Penais e Observações")
        st.markdown("""
        * **Crime Ambiental (Lei 9.605/98, Art. 56):** Transporte de substância tóxica em desacordo com as exigências regulamentares, expondo a risco a incolumidade pública.
        * **Falsidade Documental (Código Penal, Art. 297/304):** Aplicável caso sejam identificadas adulterações em certificados físicos ou digitais.
        """)
        
        if st.button("Prosseguir com a Inspeção do Veículo ➡️"):
            st.session_state.fluxo = 'documentacao_tecnica'
            st.rerun()

# =========================================================
# CERTIFICAÇÕES TÉCNICAS (CONJUNTO VEICULAR)
# =========================================================
elif st.session_state.fluxo == 'documentacao_tecnica':
    st.header("Certificações Técnicas do Equipamento")
    
    if st.button("⬅️ Retornar"):
        st.session_state.fluxo = 'condutor'
        st.rerun()

    st.markdown("---")
    st.write("Dando continuidade ao rito, procederemos agora com a análise do CIV e CIPP...")
