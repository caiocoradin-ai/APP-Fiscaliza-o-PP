import streamlit as st
import pandas as pd

# Configuração da Página
st.set_page_config(page_title="PRF - Fiscalização PP", layout="centered")

# 1. Carregar a Planilha
@st.cache_data
def carregar_dados():
    try:
        df = pd.read_csv("produtos_onu.csv")
        return df
    except:
        return None

df_onu = carregar_dados()

st.title("🚓 Fiscalização de Produtos Perigosos")
st.subheader("MPO-005: Identificação e Isenção")

if df_onu is not None:
    # 2. Busca do Produto
    busca = st.text_input("Busque pelo Número ONU ou Nome (Ex: 1203)")

    if busca:
        resultado = df_onu[
            (df_onu['onu'].astype(str).str.contains(busca)) | 
            (df_onu['nome'].str.contains(busca.upper()))
        ]
        
        if not resultado.empty:
            for index, row in resultado.iterrows():
                with st.expander(f"📦 ONU {row['onu']} - {row['nome']}", expanded=True):
                    st.write(f"**Classe de Risco:** {row['classe']}")
                    st.write(f"**Limite Coluna 8:** {row['limite_coluna8']} kg/L")
                    
                    # 3. Lógica de Cálculo de Peso
                    st.divider()
                    st.markdown("### ⚖️ Verificação de Peso (NF)")
                    peso_nf = st.number_input(f"Peso Bruto Total do ONU {row['onu']} (kg/L):", min_value=0.0, step=1.0, key=f"peso_{index}")

                    limite = float(row['limite_coluna8'])

                    if peso_nf > 0:
                        if limite == 0:
                            st.error(f"🚨 **NÃO HÁ ISENÇÃO:** Para o ONU {row['onu']}, qualquer quantidade exige sinalização completa e curso MOPP.")
                        elif peso_nf > limite:
                            st.error(f"🚨 **NÃO ISENTO:** Peso ({peso_nf}kg) acima do limite de {limite}kg. Exigir Sinalização e MOPP.")
                        else:
                            st.success(f"✅ **ISENTO DE SINALIZAÇÃO E MOPP:** Peso ({peso_nf}kg) está dentro do limite de {limite}kg.")
                            st.info("⚠️ **Obrigatório:** Extintor de 2kg e frase 'QUANTIDADE LIMITADA' no documento fiscal.")
        else:
            st.error("Produto não encontrado.")
else:
    st.error("Erro ao carregar a base de dados.")
