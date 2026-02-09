import streamlit as st
import pandas as pd

# CONFIGURAÇÃO
st.set_page_config(page_title="Bizuário PRF - Passo a Passo", layout="centered", page_icon="🚓")

# Estilo para botões e textos
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; font-weight: bold; }
    .explicacao { background-color: #e1e5eb; padding: 15px; border-radius: 10px; margin-bottom: 20px; border-left: 5px solid #002244; }
    .status-ok { color: green; font-weight: bold; }
    .status-erro { color: red; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# Inicialização da memória de infrações
if 'checklist' not in st.session_state:
    st.session_state.checklist = {}

# 1. IDENTIFICAÇÃO (Sempre visível no topo)
st.title("🚓 Guia de Fiscalização PP")
onu = st.text_input("Digite o Número ONU (Ex: 1203):", "")

if onu:
    st.divider()
    
    # ABAS COMO ETAPAS
    abas = st.tabs(["👤 Equipe", "⏱️ Jornada", "📄 Documentos", "📦 Carga", "🚨 Resumo"])

    # --- ETAPA 1: EQUIPE ---
    with abas[0]:
        st.markdown('<div class="explicacao"><b>O QUE É:</b> Verificação do condutor e auxiliares. A norma proíbe carona e exige traje adequado (calça, camisa e sapato) para segurança em caso de vazamento.</div>', unsafe_allow_html=True)
        
        st.subheader("O condutor possui curso MOPP e todos estão trajados adequadamente?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ SIM", key="equipe_sim"):
                st.session_state.checklist['equipe'] = "OK"
        with col2:
            if st.button("❌ NÃO", key="equipe_nao"):
                st.session_state.checklist['equipe'] = "ERRO"
        
        if st.session_state.checklist.get('equipe') == "ERRO":
            st.error("🚨 **INFRAÇÃO:** Art. 43, II, 'a' ou 'b' (Res. 5998/22). \n\n**O que fazer:** Autuar o transportador. O traje é Equipamento de Proteção individual.")

    # --- ETAPA 2: JORNADA ---
    with abas[1]:
        st.markdown('<div class="explicacao"><b>O QUE É:</b> Controle de fadiga (Lei 13.103/15). O descanso é essencial para evitar acidentes catastróficos com carga perigosa.</div>', unsafe_allow_html=True)
        
        st.subheader("O tempo de direção e descanso está correto no disco/fita?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ SIM", key="jor_sim"):
                st.session_state.checklist['jornada'] = "OK"
        with col2:
            if st.button("❌ NÃO", key="jor_nao"):
                st.session_state.checklist['jornada'] = "ERRO"

        if st.session_state.checklist.get('jornada') == "ERRO":
            st.warning("⚠️ **AVISO:** Só autuar (Art. 230, XXIII CTB) se o trecho da Delegacia possuir Ponto de Parada (PPD) cadastrado!")

    # --- ETAPA 3: DOCUMENTOS ---
    with abas[2]:
        st.markdown('<div class="explicacao"><b>O QUE É:</b> Verificação da Nota Fiscal e Certificados (CIV/CIPP). A NF deve ter a "Declaração do Expedidor" para garantir que a carga foi bem montada.</div>', unsafe_allow_html=True)
        
        st.subheader("A NF tem a Declaração do Expedidor e os Certificados estão válidos?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ SIM", key="doc_sim"):
                st.session_state.checklist['docs'] = "OK"
        with col2:
            if st.button("❌ NÃO", key="doc_nao"):
                st.session_state.checklist['docs'] = "ERRO"

        if st.session_state.checklist.get('docs') == "ERRO":
            st.error("🚨 **INFRAÇÃO:** Art. 43, III, 'a' (Falta de Declaração) ou Art. 43, II, 'f' (CIV/CIPP vencido).")

    # --- ETAPA 4: CARGA ---
    with abas[3]:
        st.markdown('<div class="explicacao"><b>O QUE É:</b> Verificação física de sinalização, vazamentos e incompatibilidade (ex: produto químico junto com alimento).</div>', unsafe_allow_html=True)
        
        st.subheader("A sinalização está correta e a carga está sem vazamentos/misturas proibidas?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ SIM", key="car_sim"):
                st.session_state.checklist['carga'] = "OK"
        with col2:
            if st.button("❌ NÃO", key="car_nao"):
                st.session_state.checklist['carga'] = "ERRO"

        if st.session_state.checklist.get('carga') == "ERRO":
            st.error("🚨 **INFRAÇÃO:** Art. 43, I (Sinalização) ou Art. 43, IV (Incompatibilidade).")

    # --- ETAPA 5: RESUMO ---
    with abas[4]:
        st.subheader("Relatório da Fiscalização")
        resumo = []
        for etapa, status in st.session_state.checklist.items():
            cor = "✅" if status == "OK" else "❌"
            resumo.append(f"{cor} {etapa.upper()}: {status}")
        
        if resumo:
            st.code("\n".join(resumo), language="text")
            if "ERRO" in str(st.session_state.checklist.values()):
                st.warning("⚠️ Foram encontradas irregularidades. Verifique os enquadramentos nas abas anteriores.")
            else:
                st.success("✅ Veículo liberado. Nenhuma irregularidade detectada.")
        else:
            st.info("Responda às perguntas nas abas anteriores para gerar o resumo.")

        if st.button("🔄 Reiniciar Fiscalização"):
            st.session_state.checklist = {}
            st.rerun()

else:
    st.info("Aguardando Número ONU para iniciar o guia...")
