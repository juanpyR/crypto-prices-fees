# 💱 Crypto Prices & Withdrawal Fees Dashboard

A Streamlit dashboard to check cryptocurrency prices and withdrawal fees on Gate.io and Binance, with multilingual support (Spanish and English).

## 🚀 Key Features

- 🔍 Real-time price lookup for cryptocurrencies (e.g., ETH, USDC, TRX) against USDT on Gate.io and Binance.
- 💸 Detailed withdrawal fees by network for each coin on both exchanges.
- 🎨 Stylish presentation with logos, professionally designed and organized HTML tables.
- 🌐 Quick language switch between Spanish and English using dedicated buttons.
- 🛠 Modular, clean, and well-organized code with reusable functions.
- 🔢 Price formatting without scientific notation using the decimal library.

## 📦 Requirements

- Python 3.8 or higher
- Internet connection (to fetch prices and fees from APIs)

To install dependencies:

```bash
pip install -r requirements.txt

📁 Project Structure  
```
├── app.py  
├── funciones.py  
├── lang_texts.py  
├── app_core.py  
├── crypto_handler.py  
├── exchange_manager.py  
├── display_handler.py  
├── language_handler.py  
├── exchanges_config.py  
└── requirements.txt
```


**app.py**  
Main file that runs the Streamlit app. Handles the interface, coin input, language switching, and price & fees display.

**funciones.py**  
Contains functions to consume APIs, process data, format prices, handle languages, and render styled HTML tables.

**lang_texts.py**  
Dictionary with translated texts for Spanish and English used throughout the app.

**app_core.py**  
Core of the application coordinating modules.

**crypto_handler.py**  
Module responsible for fetching prices and fees from APIs.

**exchange_manager.py**  
Manages fetching and unifying data from exchanges.

**display_handler.py**  
Handles rendering visual elements in Streamlit.

**language_handler.py**  
Module for language management.

**requirements.txt**  
List of dependencies to install.

**exchanges_config.py**  
Information of exchanges

## ▶️ How to Run

1. Clone this repository:

```bash
git clone https://github.com/juanpyR/crypto-prices-fees.git
cd crypto-prices-fees

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the app:

```
streamlit run app.py
```

4. The app will open automatically at `http://localhost:8501` (or another available port) in your browser.

---
## 🖼 Screenshots

### 🔎 Search Panel
![Search](https://raw.githubusercontent.com/juanpyR/crypto-prices-fees/main/images/search.png)

### 💸 Withdrawal Fees
![Fees](https://raw.githubusercontent.com/juanpyR/crypto-prices-fees/main/images/fees.png)

### 🙏 Donation Prompt
![Donation](https://raw.githubusercontent.com/juanpyR/crypto-prices-fees/main/images/donation.png)

## 🤝 Contributions
Contributions are welcome! If you find bugs or have ideas, please open an issue or submit a pull request.

## 📄 License
MIT License – you're free to use, modify, and distribute this project.
