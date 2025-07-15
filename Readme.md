# 🚀 Crypto Prices & Withdrawal Fees Dashboard

A Streamlit dashboard to check cryptocurrency prices and withdrawal fees on Gate.io and Binance, with multilingual support (Spanish and English).

## ✨ Main Features

- 🔍 Real-time price lookup for cryptocurrencies (e.g., ETH, USDC, TRX) against USDT on Gate.io and Binance.
- 💸 Detailed withdrawal fees by network for each coin on both exchanges.
- 🎨 Stylish presentation with logos, professionally designed and organized HTML tables.
- 🌐 Quick language switch between Spanish and English using dedicated buttons.
- 🛠 Modular, clean, and well-organized code with reusable functions.
- 🔢 Price formatting without scientific notation using the decimal library.

## 💻 Technologies Used

- Python 3.8+
- Streamlit
- Requests
- Pandas
- Decimal (for numeric formatting)
- HTML/CSS (for styling tables and presentation)

## 📁 Project Structure

├── app.py
Main file that runs the Streamlit app.
Handles the interface, coin input, language switching, and price & fees display.

├── funciones.py
Contains functions to consume APIs, process data, format prices, handle languages, and render styled HTML tables.

├── lang_texts.py
Dictionary with translated texts for Spanish and English used throughout the app.

├── app_core.py
Core of the application coordinating modules.

├── crypto_handler.py
Module responsible for fetching prices and fees from APIs.

├── exchange_manager.py
Manages fetching and unifying data from exchanges.

├── display_handler.py
Handles rendering visual elements in Streamlit.

├── language_handler.py
Module for language management.

└── requirements.txt
List of dependencies to install.

Important note:
The exchanges_config.py file containing specific exchange configurations is private and not included in this repository

✅ Requirements
Python 3.8 or higher

Internet connection (to fetch prices and fees from APIs)

📄 License
This project is licensed under the MIT License. Feel free to use, modify, and share it freely.

🙏 Credits
Developed with ❤️ by [Juan]
