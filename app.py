import streamlit as st
import pandas as pd
from pathlib import Path

GOLD_PATH = Path("data/gold/sih_kpis.csv")
SILVER_PATH = Path("data/silver/sih_silver.csv")


st.set_page_config(
    page_title="InsightFlow AI",
    layout="wide"
)

# -----------------------
# HEADER
# -----------------------
st.title("🏥 InsightFlow AI")
st.subheader("Health Analytics Dashboard (SIH - Brazil)")

st.markdown("""
Sistema de análise de dados de saúde pública com pipeline ETL (Bronze → Silver → Gold)
e geração de KPIs para apoio à decisão.
""")

# -----------------------
# LOAD DATA
# -----------------------
@st.cache_data
def load_kpis():
    if GOLD_PATH.exists():
        return pd.read_csv(GOLD_PATH)
    return None


kpis = load_kpis()

# -----------------------
# KPIs SECTION
# -----------------------
st.divider()
st.header("📊 Indicadores Gerais")

if kpis is None:
    st.warning("Nenhum KPI encontrado. Execute o pipeline primeiro.")
else:
    col1, col2, col3 = st.columns(3)

    with col1:
        total = kpis["total_hospitalizations"].sum()
        st.metric("Total de Internações", f"{total:,}")

    with col2:
        avg_cost = kpis["avg_cost"].mean()
        st.metric("Custo Médio", f"R$ {avg_cost:,.2f}")

    with col3:
        avg_stay = kpis["avg_length_stay"].mean()
        st.metric("Tempo Médio de Internação", f"{avg_stay:.1f} dias")

# -----------------------
# TABLE
# -----------------------
st.divider()
st.header("📈 Internações por Estado")

if kpis is not None:
    chart_data = kpis.groupby("state")["total_hospitalizations"].sum()
    st.bar_chart(chart_data)

st.header("🦠 Internações por Doença")

disease_data = kpis.groupby("disease")["total_hospitalizations"].sum()
st.bar_chart(disease_data)

# -----------------------
# CHART
# -----------------------
st.divider()
st.header("📈 Internações por Estado")

if kpis is not None:
    chart_data = kpis.set_index("state")["total_hospitalizations"]
    st.bar_chart(chart_data)

# -----------------------
# FOOTER ACTION
# -----------------------
st.divider()
st.caption("InsightFlow AI - Data Engineering + Analytics + AI (MVP)")