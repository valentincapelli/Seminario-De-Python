import streamlit as st
from PIL import Image

icon = Image.open("icon.png")
st.set_page_config(page_title="Inicio", page_icon=icon, layout="wide")