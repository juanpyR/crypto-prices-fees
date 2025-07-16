import streamlit as st
from display_handler import DisplayHandler
from exchange_manager import ExchangeManager
from crypto_handler import CryptoHandler
from lang_texts import TEXTOS
from exchanges_config import EXCHANGES_CONFIG

class AppCore:
    def __init__(self):
        self.display = DisplayHandler()
        self.crypto_handler = CryptoHandler()
        self.exchange_mgr = ExchangeManager(self.crypto_handler, EXCHANGES_CONFIG)

        if "moneda_input" not in st.session_state:
            st.session_state["moneda_input"] = ""
        if "moneda" not in st.session_state:
            st.session_state["moneda"] = ""

    def manejar_idiomas(self):
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🌐 Español"):
                st.session_state.idioma = "es"
        with col2:
            if st.button("🌐 English"):
                st.session_state.idioma = "en"

        idioma = st.session_state.get("idioma", "es")
        return TEXTOS[idioma]

    def run(self):
        textos = self.manejar_idiomas()

        st.title(textos["titulo"])

        self.display.render_moneda_input(textos["texto_input"])

        def buscar():
            st.session_state["moneda"] = st.session_state["moneda_input"].strip().upper()

        st.button(textos["boton_buscar"], on_click=buscar, key="btn_buscar_seguro")

        moneda = st.session_state.get("moneda", "")
        if moneda:
            if moneda == "USDT":
                st.info(textos["mensaje_sin_precio_usdt"])
                self.exchange_mgr.mostrar_fees_unificadas(moneda, textos, self.display)
            else:
                self.exchange_mgr.mostrar_precios(moneda, textos, self.display)
                self.exchange_mgr.mostrar_fees_unificadas(moneda, textos, self.display)

        st.markdown("---")
        self.display.mostrar_boton_donar_usdt_solana(textos)
