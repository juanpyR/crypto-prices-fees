import streamlit as st
import pandas as pd

class DisplayHandler:
    def __init__(self):
        pass

    def render_header(self, texto):
        st.header(texto)

    def render_warning(self, texto):
        st.warning(texto)

    def render_moneda_input(self, texto_input):
        st.markdown(self.custom_css(), unsafe_allow_html=True)
        st.markdown(f'<div class="custom-label">{texto_input}</div>', unsafe_allow_html=True)
        st.text_input("", value=st.session_state.get("moneda_input", ""), key="moneda_input")

    def custom_css(self):
        return """
        <style>
        .custom-label {
            font-size: 18px;
            font-weight: 600;
            color: #064420;
            margin-top: 12px;
            margin-bottom: 8px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            cursor: default;
        }
        input[type="text"] {
            color: #000000 !important;           
            background-color: #f0fff0 !important; 
            border: 2px solid #064420 !important; 
            border-radius: 6px !important;
            padding: 8px !important;
            font-size: 16px !important;
            outline: none !important;
        }
        input[type="text"]:focus {
            border-color: #0b8e4a !important;
            box-shadow: 0 0 5px #0b8e4a !important;
            background-color: #e6ffe6 !important;
        }
        button[kind="primary"] {
            background-color: #064420 !important;
            color: white !important;
            border-radius: 6px !important;
            padding: 10px 20px !important;
            font-weight: 600 !important;
            font-size: 16px !important;
            border: none !important;
            cursor: pointer !important;
            transition: background-color 0.3s ease !important;
        }
        button[kind="primary"]:hover {
            background-color: #0b8e4a !important;
        }
        table {
            border-collapse: collapse; 
            width: 100%; 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 14px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        th {
            background-color: #009879;
            color: white;
            text-align: center;
            padding: 12px 15px;
        }
        td {
            text-align: center;
            border-bottom: 1px solid #ddd;
            padding: 10px;
        }
        </style>
        """

    def render_precio_formateado(self, logo_url, nombre_exchange, precio):
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; font-size: 16px; line-height: 1.2; margin-bottom: 10px;">
                <img src="{logo_url.strip()}" width="40" style="margin-right: 10px; object-fit: contain;" />
                <div>
                    <span style="font-weight: 600; color: #444;">{nombre_exchange}</span>:&nbsp;
                    <span style="color: #0a7c00;">{precio} USDT</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    def render_tabla_fees_unificada(self, df_fees_unificada):
        filas_html = "<tr style='background-color:#009879; color:white; text-align:center;'>"
        for col in df_fees_unificada.columns:
            filas_html += f"<th style='padding:12px 15px'>{col}</th>"
        filas_html += "</tr>"
    
        for _, fila in df_fees_unificada.iterrows():
            filas_html += "<tr style='text-align:center; border-bottom:1px solid #ddd;'>"
            for val in fila:
                filas_html += f"<td style='padding:10px'>{val}</td>"
            filas_html += "</tr>"
    
        tabla_html = f"""
        <table style="
            border-collapse: collapse; 
            width: 100%; 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 14px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        ">
            {filas_html}
        </table>
        """

        st.markdown(tabla_html, unsafe_allow_html=True)
        
    def render_minimos_por_exchange(self, df_fees_unificada, moneda,textos, formatear_func):
        st.markdown(f"### {textos['titulo_minimos_fees']}")
    
        for col in df_fees_unificada.columns[1:]:  # Omitimos 'Network'
            fees_col = pd.to_numeric(df_fees_unificada[col], errors='coerce')
    
            if fees_col.notna().any():
                min_val = fees_col.min()
                redes_minimas = df_fees_unificada[fees_col == min_val]["Network"].tolist()
    
                min_val_str = formatear_func(min_val)
    
                redes_str = ", ".join(redes_minimas)
                st.success(textos["mensaje_minimo_fee"].format(col, min_val_str, moneda.upper(), redes_str))
            else:
                st.warning(textos["mensaje_no_datos"].format(col))           
             
    def _get_logo_url(self, exchange_name):
        # Aquí defines los logos de cada exchange para mostrar en encabezado (puedes importar de config)
        logos = {
            "gate": "https://images.seeklogo.com/logo-png/61/1/gate-io-icon-logo-png_seeklogo-617830.png",
            "binance": "https://images.seeklogo.com/logo-png/32/1/binance-coin-bnb-logo-png_seeklogo-325081.png",
            # Agrega más exchanges si quieres
        }
        return logos.get(exchange_name, None)

    def mostrar_boton_donar_usdt_solana(self, textos):
        st.header(textos['header_donacion'])
        st.markdown(f"**{textos['texto_donacion']}**")
        st.code(textos["direccion_donacion"])
        st.info(textos["mensaje_donacion"])
