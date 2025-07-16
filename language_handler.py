import streamlit as st
from lang_texts import TEXTOS

class LanguageHandler:
    def __init__(self):
        self.idioma = st.session_state.get("idioma", "es")

    def manejar_idioma(self):
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🌐 Español"):
                st.session_state.idioma = "es"
        with col2:
            if st.button("🌐 English"):
                st.session_state.idioma = "en"

        self.idioma = st.session_state.get("idioma", "es")
        return TEXTOS[self.idioma]
