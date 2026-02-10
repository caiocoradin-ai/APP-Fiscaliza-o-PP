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
    Este sistema foi desenvolvido pelo **Núcleo de Segurança Viária (NSV) da PRF no Rio Grande do Norte** para suporte técnico à fiscalização.
    """)
    
    if st.button("🚀 Iniciar Procedimento de Fiscalização"):
        st.session_state.fluxo = 'condutor'
        st.rerun()

# =========================================================
# IDENTIFICAÇÃO E REGULARIDADE DO CONDUTOR (CNH/CURSO)
# =========================================================
elif st.session_state.fluxo == 'condutor':
    st.header("Qualificação Profissional do Condutor")
    
    # 1. VALIDADE DA CNH
    st.subheader("Validação Cronológica da CNH")
    cnh_validade = st.radio("A CNH encontra-se no prazo de validade?", 
                            ["Em análise", "Sim", "Não (Vencida há mais de 30 dias)"])
    if cnh_validade == "Não (Vencida há mais de 30 dias)":
        st.error("🚨 Art. 162, V do CTB.")

    st.markdown("---")

    # 2. CATEGORIA DA CNH
    st.subheader("Compatibilidade de Categoria")
    cnh_categoria = st.radio("A categoria é compatível com o conjunto?", 
                             ["Em análise", "Sim", "Não (Incompatível)"])
    if cnh_categoria == "Não (Incompatível)":
        st.error("🚨 Art. 162, III do CTB.")

    st.markdown("---")

    # 3. CURSO TÉCNICO (CETPP)
    st.subheader("Curso Especializado (CETPP)")
    status_mopp = st.radio("O curso técnico consta como ativo/averbado?", 
                           ["Em análise", "Sim", "Não (Irregular)"])

    if status_mopp == "Sim":
        st.success("Habilitação técnica confirmada.")
        if st.button("Avançar para Trajes e Caronas ➡️"):
            st.session_state.fluxo = 'trajes_caronas'
            st.rerun()
    elif status_mopp == "Não (Irregular)":
        st.error("🚨 Infrações: Art. 162, VII CTB / Art. 43 ANTT (Transportador e Expedidor).")
        if st.button("Prosseguir com a Fiscalização ➡️"):
            st.session_state.fluxo = 'trajes_caronas'
            st.rerun()

# =========================================================
# TRAJES E CARONAS (ART. 22 E ART. 17 RTRPP)
# =========================================================
elif st.session_state.fluxo == 'trajes_caronas':
    st.header("Verificação de Trajes e Passageiros")
    
    if st.button("⬅️ Voltar"):
        st.session_state.fluxo = 'condutor'
        st.rerun()

    st.markdown("---")

    # 1. VERIFICAÇÃO DE TRAJES (Art. 22 RTRPP)
    st.subheader("Vestuário do Condutor e Auxiliares")
    
    with st.expander("📄 Requisito Legal (Art. 22 RTRPP)", expanded=True):
        st.markdown("""
        **Trajes mínimos obrigatórios:**
        * Calça comprida;
        * Camisa ou camiseta (mangas curtas ou compridas);
        * Calçados fechados.
        """)

    traje_ok = st.radio("O condutor e ajudantes estão adequadamente trajados?", 
                        ["Em análise", "Sim (Conforme Art. 22)", "Não (Desconformidade identificada)"])

    if traje_ok == "Não (Desconformidade identificada)":
        st.error("🚨 **Infração (ANTT):** Art. 43, §4º, X.")
        st.info("**Responsabilidade:** Transportador.")
        st.warning("⚠️ **Medida Administrativa:** O veículo só deverá prosseguir após a regularização dos trajes.")

    st.markdown("---")

    # 2. PROIBIÇÃO DE CARONAS (Art. 17, I RTRPP)
    st.subheader("Presença de Passageiros (Caronas)")
    
    st.info("É proibido conduzir pessoas além dos auxiliares, salvo se disposto em contrário nas Instruções Complementares.")

    caronas = st.radio("Foram constatados 'caronas' ou pessoas não autorizadas no veículo?", 
                       ["Em análise", "Não (Apenas condutor e auxiliares)", "Sim (Presença de pessoas não autorizadas)"])

    if caronas == "Sim (Presença de pessoas não autorizadas)":
        st.error("🚨 **Infração (ANTT):** Art. 43, §3º, XII.")
        st.info("**Responsabilidade:** Transportador.")
        st.warning("⚠️ **Ação:** Retirada dos passageiros não autorizados para prosseguimento da viagem.")

    st.markdown("---")
    
    if st.button("Avançar para Certificações Técnicas (CIV/CIPP) ➡️"):
        st.session_state.fluxo = 'documentacao_tecnica'
        st.rerun()

# Espaço reservado para a próxima etapa
elif st.session_state.fluxo == 'documentacao_tecnica':
    st.header("Certificações Técnicas (CIV e CIPP)")
    if st.button("⬅️ Retornar"):
        st.session_state.fluxo = 'trajes_caronas'
        st.rerun()
