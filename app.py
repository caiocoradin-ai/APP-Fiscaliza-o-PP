import streamlit as st

# Configuração da página para garantir que não corte o texto em telas menores
st.set_page_config(page_title="Bizuário PP - PRF", layout="centered")

# Inicialização do controle de navegação
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'Etapa 0'

# Título do Aplicativo
st.title("🛡️ Fiscalização de Produtos Perigosos")
st.caption("Versão Digital do Bizuário Técnico - 2026")
st.markdown("---")

# =========================================================
# ETAPA 0: INÍCIO DA ABORDAGEM (CONDUTOR)
# =========================================================
if st.session_state.pagina == 'Etapa 0':
    st.header("Etapa 0: Início da Abordagem (Condutor)")
    
    st.subheader("Passo 2.4: O condutor possui o Curso Especializado de Transporte de Produtos Perigosos (CETPP) válido e averbado?")
    
    with st.expander("📝 Ação Recomendada", expanded=True):
        st.write("Verifique na CNH Digital ou pelo CPF no aplicativo 'Fiscalização Senatran'. A informação deve estar na base RENACH.")

    # Opções de Seleção
    mopp_status = st.radio("Selecione o status do curso:", 
                           ["Aguardando Verificação", "Sim (Curso ativo no sistema)", "Não (Curso vencido, inexistente ou não averbado)"])

    if mopp_status == "Sim (Curso ativo no sistema)":
        st.success("Condutor regularizado.")
        if st.button("Avançar para Etapa 1 ➡️"):
            st.session_state.pagina = 'Etapa 1'
            st.rerun()

    elif mopp_status == "Não (Curso vencido, inexistente ou não averbado)":
        st.error("🚨 Detalhamento das Infrações (Em caso de 'NÃO'):")
        
        st.markdown("### 1. Esfera de Trânsito (CTB):")
        st.info("**Art. 162, VII:** Dirigir veículo sem possuir os cursos especializados previstos no CTB.\n\n**Resumo:** Infração específica para o condutor que não comprova a formação técnica exigida para a carga.")
        
        st.markdown("### 2. Esfera de Transporte (Res. 5.998/22 ANTT):")
        st.markdown("""
        **Art. 43, §2º, XIX ou XX (Transportador):** Transportar produtos perigosos com condutor que não possua curso especializado ou com curso vencido.
        * **Resumo:** Responsabilidade da empresa transportadora por permitir que condutor sem o CETPP realize a viagem.
        
        **Art. 43, §6º, XIII ou XXIV (Expedidor):** Expedir produtos perigosos em veículo cujo condutor não possua o curso especializado exigido.
        * **Resumo:** Responsabilidade de quem envia a carga por não conferir a habilitação técnica do motorista no ato do carregamento.
        """)

        st.warning("⚖️ Enquadramentos Criminais (Campo de Observações):")
        st.markdown("""
        **Crime Ambiental (Art. 56 da Lei 9.605/98):**
        * **O que é:** Transportar substância tóxica ou nociva em desacordo com as exigências estabelecidas em leis ou regulamentos.
        * **Quando usar:** Quando a falta do curso, somada às condições da carga, configurar uma situação de grande risco à saúde ou ao meio ambiente.

        **Falsificação de Documento Público (Art. 297 CP) / Uso de Documento Falso (Art. 304 CP):**
        * **O que é:** Falsificar, alterar ou fazer uso de papéis falsificados.
        * **Quando usar:** No caso do condutor apresentar um certificado de curso flagrantemente falso ou com sinais de adulteração.
        """)
        
        if st.button("Prosseguir mesmo com Infração ➡️"):
            st.session_state.pagina = 'Etapa 1'
            st.rerun()

# Espaço reservado para as próximas etapas
elif st.session_state.pagina == 'Etapa 1':
    st.header("Etapa 1: Documentação Específica")
    st.write("Aguardando o conteúdo da Etapa 1 (CIV/CIPP)...")
    if st.button("⬅️ Voltar"):
        st.session_state.pagina = 'Etapa 0'
        st.rerun()
