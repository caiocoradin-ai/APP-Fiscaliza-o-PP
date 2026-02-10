import streamlit as st

# Configuração da página
st.set_page_config(page_title="Bizuário PP - PRF", layout="centered")

# Inicialização do controle de navegação e estado
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'Inicio'

# =========================================================
# TELA DE INÍCIO: LINGUAGEM FORMAL E DIRETRIZES
# =========================================================
if st.session_state.pagina == 'Inicio':
    st.title("🛡️ Sistema de Apoio à Fiscalização")
    st.subheader("Transporte Rodoviário de Produtos Perigosos")
    
    st.markdown("""
    Prezado colega, 
    
    Este sistema foi desenvolvido para subsidiar a fiscalização técnica de veículos transportando produtos perigosos, garantindo a correta aplicação da **Resolução ANTT nº 5.998/22** e do **Código de Trânsito Brasileiro**.

    **Escopo da Fiscalização:**
    O procedimento está estruturado nas seguintes etapas sequenciais:
    
    1.  **Habilitação Técnica:** Verificação do condutor e validade do CETPP (MOPP).
    2.  **Certificação do Conjunto:** Análise dos certificados CIV e CIPP (para transporte a granel).
    3.  **Documentação de Transporte:** Conferência de Nota Fiscal, Declaração do Expedidor e cálculo automático de isenções/quantidades limitadas.
    4.  **Equipamentos de Segurança:** Inspeção de EPIs e Kit de Emergência.
    5.  **Sinalização e Acondicionamento:** Verificação de painéis de segurança, rótulos de risco e estiva da carga.
    6.  **Relatório de Desfecho:** Compilação final de todos os enquadramentos, medidas administrativas e infrações identificadas.
    """)
    
    if st.button("🚀 Iniciar Procedimento de Fiscalização"):
        st.session_state.pagina = 'Etapa 0'
        st.rerun()

# =========================================================
# ETAPA 0: INÍCIO DA ABORDAGEM (CONDUTOR)
# =========================================================
elif st.session_state.pagina == 'Etapa 0':
    st.header("Etapa 0: Identificação do Condutor")
    
    st.subheader("Passo 2.4: Verificação do Curso Especializado (CETPP)")
    
    with st.expander("📝 Procedimento Operacional", expanded=True):
        st.write("Realize a consulta via CNH Digital ou através do CPF no sistema 'Fiscalização Senatran'. A validade e a averbação devem constar na base RENACH.")

    # Opções de Seleção
    mopp_status = st.radio("Status do curso no sistema:", 
                           ["Aguardando Verificação", "Regular (Curso ativo e averbado)", "Irregular (Vencido, inexistente ou não averbado)"])

    if mopp_status == "Regular (Curso ativo e averbado)":
        st.success("Habilitação técnica confirmada.")
        if st.button("Avançar para Etapa 1 (Documentação Técnica) ➡️"):
            st.session_state.pagina = 'Etapa 1'
            st.rerun()

    elif mopp_status == "Irregular (Vencido, inexistente ou não averbado)":
        st.error("🚨 Identificação de Irregularidade:")
        
        st.markdown("### 1. Esfera de Trânsito (CTB):")
        st.info("**Art. 162, VII:** Conduzir veículo sem possuir os cursos especializados previstos no CTB.\n\n**Resumo:** Infração imputada ao condutor pela ausência de comprovação da formação técnica exigida.")
        
        st.markdown("### 2. Esfera de Transporte (Res. 5.998/22 ANTT):")
        st.markdown("""
        **Art. 43, §2º, XIX ou XX (Transportador):** Transportar produtos perigosos com condutor desprovido de curso especializado ou com validade expirada.
        * **Análise:** Responsabilidade do transportador por permitir a operação por condutor não habilitado tecnicamente.
        
        **Art. 43, §6º, XIII ou XXIV (Expedidor):** Expedir produtos perigosos em veículo cujo condutor não possua o curso especializado exigido.
        * **Análise:** Responsabilidade do expedidor pela falha na conferência documental no ato do carregamento.
        """)

        st.warning("⚖️ Enquadramentos Criminais e Observações:")
        st.markdown("""
        **Lei nº 9.605/98, Art. 56 (Crime Ambiental):**
        * Configura-se ao transportar substância tóxica ou nociva em desacordo com as exigências legais, resultando em perigo à saúde pública ou ao meio ambiente.

        **Código Penal, Art. 297 e 304 (Falsidade Documental):**
        * Aplicável em situações de detecção de certificados com indícios de contrafação ou adulteração.
        """)
        
        if st.button("Prosseguir com a Fiscalização ➡️"):
            st.session_state.pagina = 'Etapa 1'
            st.rerun()

# =========================================================
# ETAPA 1: DOCUMENTAÇÃO ESPECÍFICA (RESERVA)
# =========================================================
elif st.session_state.pagina == 'Etapa 1':
    st.header("Etapa 1: Certificações Técnicas (CIV/CIPP)")
    st.write("Aguardando inserção de dados conforme o rito da fiscalização...")
    
    if st.button("⬅️ Retornar à Etapa Anterior"):
        st.session_state.pagina = 'Etapa 0'
        st.rerun()
