import streamlit as st

logo = "images/azure_ai_logo.png"

st.logo(logo, size="large")
st.set_page_config(
    page_title="Azure AI Demos",
    page_icon="🧠",
)

st.title("Getting started")
st.subheader(
    """
    **👈 Select a module from the sidebar** to see some examples 
"""
)

st.page_link("Home.py", label="Home", icon="🏠")
st.page_link("pages/01-👀 Computer Vision.py", label="Module 1 - Computer Vision", icon="👀")
st.page_link("pages/02-🔠 Language.py", label="Module 2 - Language", icon="🔠")
st.page_link("pages/03-🔎 Knowledge Mining.py", label="Module 3 - Knowledge Mining", icon="⛏️")
st.page_link("pages/04-🦾GenerativeAI.py", label="Module 4 - Generative AI", icon="🦾")
st.page_link("pages/05-📑Document Intelligence.py", label="Module 5 - Document Intelligence", icon="📑")

