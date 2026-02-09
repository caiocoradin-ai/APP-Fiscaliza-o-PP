import streamlit as st

st.set_page_config(page_title="PRF - Fiscalização PP", layout="centered")

st.title("🚓 Fiscalização de Produtos Perigosos")
st.write("### Baseado no MPO-005 (Março/2025)")

# Campo de entrada
onu = st.text_input("Digite o Número ONU (Ex: 1203)")

if onu == "1203":
    st.info("⛽ **Produto: GASOLINA**")
    st.write("**Classe de Risco:** 3 (Líquido Inflamável)")
    st.write("**Limite Coluna 8:** 1000kg")
    
    peso = st.number_input("Peso da Carga (kg)", min_value=0.0)
    if peso > 1000:
        st.error("🚨 NÃO ISENTO: Exigir MOPP e Sinalização.")
    else:
        st.success("✅ ISENTO: Apenas extintor e frase 'Quant. Ltda' na NF.")

st.divider()
st.write("Desenvolvido para apoio operacional PRF.")
