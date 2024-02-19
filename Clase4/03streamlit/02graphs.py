import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title = "Streamlit - Estadísticas", page_icon = "📊")

st.title("Gráficos estadísticos con Streamlit")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns = ["a", "b", "c"])

st.line_chart(chart_data)

st.scatter_chart(chart_data)

st.bar_chart(chart_data)

st.table(chart_data)