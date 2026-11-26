import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Dar Zinab Direct (projet pédagogique fictif)", layout="wide")

# Réduit les marges de Streamlit pour que le site occupe toute la largeur
st.markdown(
    "<style>.block-container{padding:0 !important;max-width:100% !important}"
    "header,footer{visibility:hidden}</style>",
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "site.html").read_text(encoding="utf-8")
components.html(html, height=2400, scrolling=True)
