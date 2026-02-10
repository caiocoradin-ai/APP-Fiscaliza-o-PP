import streamlit as st

# Configuração da interface
st.set_page_config(page_title="Fiscalização de PP - NSV/RN", layout="centered")

# Controle de fluxo interno - MANTIDO INTACTO
if 'fluxo' not in st.session_state:
    st.session_state.fluxo = 'abertura'

# =========================================================
# PROTOCOLO DE ABERTURA - NSV/RN (CONGELADO)
# =========================================================
if st.session_state.fluxo == 'abertura':
    st.title("🛡️ Fiscalização de Transporte de Produtos Perigosos")
    st.markdown("---")
    
    st.markdown("### Informativo Institucional")
    st.write("""
    Este sistema foi desenvolvido pelo **Núcleo de Segurança Viária (NSV) da PRF no Rio Grande do Norte** para servir como ferramenta de suporte à decisão durante a fiscalização de veículos que transportam produtos perigosos.

    Prezado colega, o objetivo deste guia é otimizar o seu tempo de pista, garantindo que todos os requisitos da **Resolução ANTT nº 5.998/22** e do **CTB** sejam conferidos com precisão técnica e segurança jurídica.
    """)

    st.markdown("#### Abrangência do Procedimento:")
    st.write("""
    * **Qualificação Profissional:** Verificação da regularidade do condutor (CNH e CETPP).
    * **Inspeção Técnica Veicular:** Validação de certificados CIV e CIPP para granéis.
    * **Controle Documental:** Análise de Notas Fiscais, Declarações do Expedidor e enquadramentos de quantidade.
    * **Segurança Operacional:** Conferência de EPIs, Conjuntos de Emergência e Sinalização Externa.
    * **Conclusão e Enquadramentos:** Relatório consolidado de infrações e medidas administrativas.
    """)
    
    if st.button("🚀 Iniciar Procedimento de Fiscalização"):
        st.session_state.fluxo = 'condutor'
        st.rerun()

# =========================================================
# 1. QUALIFICAÇÃO PROFISSIONAL DO CONDUTOR (CONGELADO)
# =========================================================
elif st.session_state.fluxo == 'condutor':
    st.header("Qualificação Profissional do Condutor")
    
    # 1.1 VALIDADE DA CNH
    st.subheader("Validação Cronológica da CNH")
    cnh_validade = st.radio("A CNH encontra-se dentro do prazo de validade?", 
                            ["Em análise", "Sim (Documento válido)", "Não (Vencida há mais de 30 dias)"])
    if cnh_validade == "Não (Vencida há mais de 30 dias)":
        # RESUMO DA INFRAÇÃO NA PARTE VERMELHA
        st.error("🚨 **Infração Gravíssima (Art. 162, V CTB):** Dirigir veículo com validade da CNH vencida há mais de 30 dias. Penalidade: Multa e Retenção do veículo até a apresentação de condutor habilitado.")

    st.markdown("---")

    # 1.2 CATEGORIA DA CNH
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
        # RESUMO DA INFRAÇÃO NA PARTE VERMELHA
        st.error("🚨 **Infração Gravíssima (Art. 162, III CTB):** Dirigir veículo com categoria diferente da qual está habilitado. Penalidade: Multa (3x) e Retenção do veículo.")

    st.markdown("---")

    # 1.3 CURSO TÉCNICO (CETPP)
    st.subheader("Curso Especializado (CETPP)")
    
    with st.expander("ℹ️ Resumo Técnico sobre o Curso", expanded=True):
        st.markdown("""
        **Base Legal:** O Curso Especializado de Transporte de Produtos Perigosos (CETPP) é requisito indispensável conforme Art. 145 do CTB, Res. 1020/25 CONTRAN e Art. 20 do RTRPP.
        
        **Nota Técnica:** Embora a resolução denomine como curso 'específico', para efeitos de autuação de trânsito, utiliza-se o termo **'especializado'**.
        
        **Comprovação:** CNH Digital ou consulta direta ao **RENACH** via 'Fiscalização Senatran'. Caso o condutor não comprove a existência do curso válido e também não seja encontrada a informação na base RENACH deverá ocorrer autuação pela falta do curso especializado prevista no art. 162 VII (CTB).
        """)

    status_mopp = st.radio("O curso técnico consta como ativo e averbado no prontuário?", 
                           ["Em análise", "Sim (Curso Regular)", "Não (Ausente / Vencido / Não averbado)"])

    if status_mopp == "Sim (Curso Regular)":
        st.success("Habilitação técnica confirmada conforme exigência legal.")
        if st.button("Avançar para Trajes e Caronas ➡️"):
            st.session_state.fluxo = 'trajes_caronas'
            st.rerun()

    elif status_mopp == "Não (Ausente / Vencido / Não averbado)":
        # RESUMO DA INFRAÇÃO NA PARTE VERMELHA
        st.error("🚨 **Infração Gravíssima (Art. 162, VII CTB):** Dirigir veículo sem possuir os cursos especializados obrigatórios. Retenção do veículo até a apresentação de condutor qualificado.")
        
        st.markdown("""
        **Enquadramentos ANTT (Res. 5.998/22):**
        * **Transportador (Art. 43, §2º, XIX/XX):** Permitir transporte por condutor sem curso especializado.
        * **Expedidor (Art. 43, §6º, XIII/XXIV):** Expedir carga sem conferir curso do condutor.
        """)

        with st.warning("⚖️ Situações Especiais (Enquadramentos Penais)"):
            st.markdown("""
            * **Crime Ambiental (Art. 56, Lei 9.605/98):** Transporte perigoso em desacordo com exigências (grande risco).
            * **Falsidade Documental (Art. 297/304 CP):** Uso de certificado falso ou adulterado.
            """)
        
        if st.button("Prosseguir para Trajes e Caronas ➡️"):
            st.session_state.fluxo = 'trajes_caronas'
            st.rerun()

# =========================================================
# 2. VERIFICAÇÃO DE TRAJES E PASSAGEIROS (CONGELADO)
# =========================================================
elif st.session_state.fluxo == 'trajes_caronas':
    st.header("Verificação de Trajes e Passageiros")
    
    if st.button("⬅️ Retornar"):
        st.session_state.fluxo = 'condutor'
        st.rerun()

    # 2.1 TRAJES
    st.subheader("Vestuário (Art. 22 RTRPP)")
    st.info("**Art. 22 do RTRPP:** Condutor e auxiliares devem usar CALÇA COMPRIDA, CAMISA/CAMISETA e CALÇADOS FECHADOS.")
    
    traje_ok = st.radio("O vestuário está em conformidade?", ["Em análise", "Sim", "Não (Desconformidade)"])
    if traje_ok == "Não (Desconformidade)":
        # RESUMO DA INFRAÇÃO NA PARTE VERMELHA
        st.error("🚨 **Infração ANTT (Art. 43, §4º, X):** Transportar produtos perigosos com condutor ou auxiliar sem o traje mínimo obrigatório. Responsabilidade: Transportador.")
        st.warning("⚠️ **Medida Administrativa:** O veículo só deverá prosseguir após a devida regularização do vestuário.")

    st.markdown("---")

    # 2.2 CARONAS
    st.subheader("Passageiros (Art. 17, I RTRPP)")
    st.write("**Art. 17, Inciso I do RTRPP:** Proibido conduzir pessoas além dos auxiliares.")
    
    caronas_detectados = st.radio("Foram constatados 'caronas'?", ["Em análise", "Não", "Sim"])
    if caronas_detectados == "Sim":
        # RESUMO DA INFRAÇÃO NA PARTE VERMELHA
        st.error("🚨 **Infração ANTT (Art. 43, §3º, XII):** Transportar pessoas não autorizadas no veículo (caronas). Responsabilidade: Transportador.")
        st.warning("⚠️ **Ação:** Retirada imediata dos passageiros para prosseguimento da viagem.")

    if st.button("Avançar para Certificações Técnicas ➡️"):
        st.session_state.fluxo = 'documentacao_tecnica'
        st.rerun()

# =========================================================
# 3. CERTIFICAÇÕES TÉCNICAS (PRONTO PARA NOVOS ACRÉSCIMOS)
# =========================================================
elif st.session_state.fluxo == 'documentacao_tecnica':
    st.header("Certificações Técnicas (CIV e CIPP)")
    if st.button("⬅️ Retorn
