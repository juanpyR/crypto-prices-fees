EXCHANGES_CONFIG = {
    "gate": {
        "logo_url": "https://images.seeklogo.com/logo-png/61/1/gate-io-icon-logo-png_seeklogo-617830.png",
        "fees": {
            "url": "https://www.gate.com/api/web/v1/withdraw/depositwithdraw/getCoinsDepositWithdrawFee?",
            "params_key": "keyword",
            "extract_list_path": ["data", "list"],
            "coin_key": "coin",
            "chains_key": "chains",
            "chain_name_key": "chain",
            "fee_key": "withdraw_txfee",
            "filter_fn": lambda chain: True,
            "headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/116.0.0.0 Safari/537.36",
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "en-US,en;q=0.9",
                "Referer": "https://www.gate.com/",
                "Origin": "https://www.gate.com",
                "Connection": "keep-alive"
            }
        },
        "prices": {
            "url": "https://api.gateio.ws/api/v4/spot/tickers",
            "columns_float": ['last'],
            "headers": {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            "col_symbol": "currency_pair",
            "price_column": "last",
            "symbol_format": "{moneda}_USDT"
        }
    },
    "binance": {
        "logo_url": "https://images.seeklogo.com/logo-png/32/1/binance-coin-bnb-logo-png_seeklogo-325081.png",
        "fees": {
            "url": "https://www.binance.com/bapi/capital/v2/public/capital/getNetworkCoinAll",
            "params_key": None,
            "extract_list_path": ["data"],
            "coin_key": "coin",
            "chains_key": "networkList",
            "chain_name_key": "network",
            "fee_key": "withdrawFee",
            "filter_fn": lambda chain: chain.get("withdrawEnable", True)
        },
        "prices": {
            "url": "https://api.binance.com/api/v3/ticker/24hr",
            "columns_float": ['lastPrice'],
            "headers": None,
            "col_symbol": "symbol",
            "price_column": "lastPrice",
            "symbol_format": "{moneda}USDT"
        }
    }
}
