import streamlit as st
from PIL import Image

icon = Image.open("icon.png")
st.set_page_config(page_title="Inicio", page_icon=icon, layout="wide")

with st.container(border=True):
    st.page_link("pages/01_Conociendo_nuestros_datos.py",label="Conociendo nuestros datos",)
    st.page_link("pages/02_Juego.py",label="Juego")
    st.page_link("pages/03_Formulario_de_registro.py",label="Formulario de registro")
    st.page_link("pages/04_Ranking.py",label="Ranking")
    st.page_link("pages/05_Seccion_de_estadisticas.py",label="Seccion de estadisticas")