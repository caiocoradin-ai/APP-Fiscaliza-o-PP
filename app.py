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
    Este sistema orienta a fiscalização técnica de veículos destinados ao transporte de produtos perigosos, em estrita observância à **Resolução ANTT nº 5.998/22** e ao **Código de Trânsito Brasileiro**.

    **Escopo do Procedimento:**
    * **Qualificação Profissional:** Validação da CNH e do curso técnico (CETPP).
    * **Inspeção Técnica Veicular:** Validação de certificados CIV e CIPP.
    * **Controle Documental:** Análise de Notas Fiscais e enquadramentos de quantidade.
    * **Segurança Operacional:** Conferência de EPIs, Emergência e Sinalização.
    * **Conclusão:** Relatório consolidado de infrações e medidas administrativas.
    """)
    
    if st.button("🚀 Iniciar Procedimento Fiscal"):
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
        st.error("🚨 Infração: Art. 162, V do CTB (CNH vencida há mais de 30 dias).")

    st.markdown("---")

    # 2. CATEGORIA DA CNH
    st.subheader("Compatibilidade de Categoria")
    with st.expander("📄 Tabela de Categorias (Resumo Técnico)", expanded=False):
        st.markdown("""
        * **Cat. A:** 2 ou 3 rodas.
        * **Cat. B:** Até 3.500 kg PBT / 8 lugares.
        * **Cat. C:** Carga acima de 3.500 kg PBT.
        * **Cat. D:** Passageiros acima de 8 lugares.
        * **Cat. E:** Combinações com unidade acoplada de 6.000 kg ou mais de PBT.
        """)
    cnh_categoria = st.radio("A categoria é compatível com o conjunto veicular?", 
                             ["Em análise", "Sim (Compatível)", "Não (Incompatível)"])

    if cnh_categoria == "Não (Incompatível)":
        st.error("🚨 Infração: Art. 162, III do CTB (Categoria divergente).")

    st.markdown("---")

    # 3. CURSO TÉCNICO (CETPP)
    st.subheader("Curso Especializado (CETPP)")
    
    with st.expander("ℹ️ Sobre o Curso Especializado (Resumo Técnico)", expanded=True):
        st.markdown("""
        **Finalidade:** O Curso Especializado de Transporte de Produtos Perigosos (CETPP) é obrigatório conforme o Art. 145 do CTB e Art. 20 do RTRPP. 
        
        **Observações Importantes:**
        * Embora a Res. 1020/25 CONTRAN utilize o termo 'específico', para fins de autuação de trânsito, o termo correto é **'especializado'**.
        * A comprovação deve ser feita via CNH Digital ou consulta ao RENACH (aplicativo Fiscalização Senatran).
        """)

    status_mopp = st.radio("O curso técnico consta como ativo e averbado no sistema?", 
                           ["Em análise", "Sim (Curso Regular)", "Não (Ausente / Vencido / Não averbado)"])

    if status_mopp == "Sim (Curso Regular)":
        st.success("Habilitação técnica confirmada.")
        if st.button("Avançar para Certificações Técnicas ➡️"):
            st.session_state.fluxo = 'documentacao_tecnica'
            st.rerun()

    elif status_mopp == "Não (Ausente / Vencido / Não averbado)":
        st.error("🚨 Constatação de Irregularidade na Qualificação:")
        
        st.markdown("### Enquadramentos Aplicáveis:")
        st.markdown("""
        **1. Trânsito (CTB):** * **Art. 162, VII:** Conduzir veículo sem os cursos especializados obrigatórios.
        
        **2. Transporte (Res. ANTT 5.998/22):**
        * **Transportador (Art. 43, §2º, XIX/XX):** Permitir operação por condutor sem curso especializado válido.
        * **Expedidor (Art. 43, §6º, XIII/XXIV):** Expedir carga sem conferir a habilitação técnica do condutor.
        """)

        with st.warning("⚖️ Implicações Penais"):
            st.markdown("""
            * **Crime Ambiental (Art. 56, Lei 9.605/98):** Transporte de substância tóxica em desacordo com as exigências legais em situações de grande risco.
            * **Falsidade Documental (Art. 297 e 304 do Código Penal):** Uso de certificado flagrantemente falso ou adulterado.
            """)
        
        if st.button("Prosseguir com a Fiscalização do Conjunto ➡️"):
            st.session_state.fluxo = 'documentacao_tecnica'
            st.rerun()

# Espaço reservado para a próxima etapa
elif st.session_state.fluxo == 'documentacao_tecnica':
    st.header("Certificações Técnicas (CIV e CIPP)")
    if st.button("⬅️ Retornar"):
        st.session_state.fluxo = 'condutor'
        st.rerun()
    st.write("Próxima análise: Inspeção técnica de veículos e equipamentos (Granéis).")
