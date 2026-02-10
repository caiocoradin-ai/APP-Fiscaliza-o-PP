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
    Prezado agente, este sistema orienta a fiscalização técnica de veículos destinados ao transporte de produtos perigosos, em estrita observância à **Resolução ANTT nº 5.998/22** e ao **Código de Trânsito Brasileiro**.

    **Escopo do Procedimento:**
    * **Qualificação Profissional:** Validação da CNH (validade e categoria) e regularidade do curso técnico (CETPP).
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
        * **Categoria A:** Veículos motorizados de duas ou três rodas, com ou sem carro lateral.
        * **Categoria B:** Veículos motorizados cujo PBT não exceda 3.500 kg e lotação não exceda 8 lugares (excluindo o condutor).
        * **Categoria C:** Veículos motorizados utilizados em transporte de carga, cujo PBT exceda 3.500 kg (Caminhão comum).
        * **Categoria D:** Veículos motorizados utilizados no transporte de passageiros, com lotação superior a 8 lugares.
        * **Categoria E:** Combinação de veículos em que a unidade tratora se enquadre nas categorias B, C ou D e a unidade acoplada (reboque/semirreboque) possua 6.000 kg ou mais de PBT, ou lotação superior a 8 lugares.
        """)
        
    cnh_categoria = st.radio("A categoria do condutor é compatível com o conjunto veicular fiscalizado?", 
                             ["Em análise", "Sim (Categoria compatível)", "Não (Categoria incompatível/divergente)"])

    if cnh_categoria == "Não (Categoria incompatível/divergente)":
        st.error("🚨 Infração Identificada: Art. 162, III do CTB (Dirigir veículo com categoria diferente da qual está habilitado).")

    st.markdown("---")

    # 3. CURSO TÉCNICO (CETPP/MOPP)
    st.subheader("Verificação do Curso Especializado (CETPP/MOPP)")
    st.info("**Procedimento:** Consultar a base RENACH via sistema 'Fiscalização Senatran' para confirmar a averbação e validade do curso técnico.")

    status_mopp = st.radio("Status da averbação técnica no sistema:", 
                           ["Em análise", "Regular (Curso ativo e averbado)", "Irregular (Vencido, ausente ou não averbado)"])

    if status_mopp == "Regular (Curso ativo e averbado)":
        st.success("Habilitação técnica e documental confirmada.")
        if st.button("Avançar para Certificações Técnicas ➡️"):
            st.session_state.fluxo = 'documentacao_tecnica'
            st.rerun()

    elif status_mopp == "Irregular (Vencido, ausente ou não averbado)":
        st.error("🚨 Constatação de Irregularidades Técnicas:")
        
        st.markdown("### Enquadramentos Jurídicos:")
        st.markdown("#### Esfera de Trânsito")
        st.write("**Art. 162, VII do CTB:** Conduzir veículo sem os cursos especializados obrigatórios.")
        
        st.markdown("#### Esfera de Transporte (ANTT)")
        st.markdown("""
        * **Responsabilidade do Transportador (Art. 43, §2º, XIX/XX):** Permitir a realização do transporte por condutor sem a devida qualificação técnica.
        * **Responsabilidade do Expedidor (Art. 43, §6º, XIII/XXIV):** Expedir carga em veículo cujo condutor não comprove a habilitação exigida.
        """)

        st.warning("⚖️ Implicações Penais e Observações")
        st.markdown("""
        * **Crime Ambiental (Lei 9.605/98, Art
