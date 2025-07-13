# 🚀 Crypto Prices & Withdrawal Fees Dashboard

Dashboard en **Streamlit** para consultar precios y fees de retiro de criptomonedas en los exchanges **Gate.io** y **Binance**, con soporte multilenguaje (Español e Inglés).

---

## ✨ Características principales

- 🔍 Consulta en tiempo real los precios de criptomonedas (ej: ETH, USDC, TRX) contra USDT en Gate.io y Binance.
- 💸 Consulta detallada de fees de retiro por red para cada moneda en ambos exchanges.
- 🎨 Presentación estilizada con logos, tablas HTML con diseño profesional y ordenadas.
- 🌐 Soporte para cambio rápido de idioma entre Español e Inglés con botones dedicados.
- 🛠 Código modular, limpio y organizado con funciones reutilizables.
- 🔢 Formateo de precios sin notación científica, usando la librería `decimal`.

---

## 💻 Tecnologías usadas

- Python 3.8+
- Streamlit
- Requests
- Pandas
- Decimal (para formateo numérico)
- HTML/CSS (para estilizar tablas y presentación)

---

## 📁 Estructura del proyecto

- `app.py`  
  Archivo principal que ejecuta la app Streamlit.  
  Controla la interfaz, entrada de moneda, cambio de idioma y despliegue de precios y fees.

- `funciones.py`  
  Contiene funciones para consumir APIs, procesar datos, formatear precios, manejar idiomas y renderizar tablas HTML con estilos.

- `lang_texts.py`  
  Diccionario con textos traducidos para Español e Inglés usados en la app.

---

## 🚀 Instalación y ejecución

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/crypto-prices-fees.git
   cd crypto-prices-fees
