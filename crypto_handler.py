import requests
import pandas as pd
from decimal import Decimal, getcontext

getcontext().prec = 30

class CryptoHandler:
    def __init__(self):
        pass

    def formatear_precio(self, valor):
        dec = Decimal(str(valor)).normalize()
        if dec < 1:
            texto = format(dec, 'f')
            return texto.rstrip('0').rstrip('.') if '.' in texto else texto
        else:
            return str(dec)

    def obtener_fees_exchanges(self, moneda, exchange, config):
        moneda = moneda.upper()
        if not config:
            return pd.DataFrame()

        info = config.get("fees")
        if not info:
            return pd.DataFrame()

        url = info["url"]
        headers = info.get("headers", {"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
        params = {info["params_key"]: moneda} if info["params_key"] else None

        try:
            r = requests.get(url, params=params, headers=headers)
            r.raise_for_status()
            data = r.json()
        except:
            return pd.DataFrame()

        monedas = data
        for key in info["extract_list_path"]:
            monedas = monedas.get(key, [])

        moneda_encontrada = next((m for m in monedas if m.get(info["coin_key"]) == moneda), None)
        if not moneda_encontrada:
            return pd.DataFrame()

        filas = []
        for chain in moneda_encontrada.get(info["chains_key"], []):
            if info["filter_fn"](chain):
                red = chain.get(info["chain_name_key"], "Desconocida")
                try:
                    fee = float(chain.get(info["fee_key"], None))
                    fee = self.formatear_precio(fee)
                except:
                    fee = None
                filas.append({"Network": red, f"{exchange.title()} fee": fee})

        df = pd.DataFrame(filas)
        if not df.empty:
            df.index = range(1, len(df) + 1)
        return df

    def obtener_precios_por_moneda(self, moneda, exchanges_config):
        moneda = moneda.upper()
        resultados = {}
    
        for exchange, cfg in exchanges_config.items():
            try:
                config = cfg.get("prices", {})
                response = requests.get(config["url"], headers=config.get("headers"))
                response.raise_for_status()
                data = response.json()
                df = pd.DataFrame(data)
    
                for col in config.get("columns_float", []):
                    if col in df.columns:
                        df[col] = df[col].astype(float)
    
                symbol_format = config.get("symbol_format", "{moneda}USDT")
                price_column = config.get("price_column", "last")
                col_symbol = config.get("col_symbol", "symbol")
    
                par = symbol_format.format(moneda=moneda)
                precios_raw = df[df[col_symbol].str.upper() == par.upper()][price_column]
    
                if not precios_raw.empty:
                    precios_formateados = precios_raw.map(self.formatear_precio)
                    resultados[exchange] = precios_formateados.reset_index(drop=True)
                else:
                    resultados[exchange] = pd.Series(dtype=str)
    
            except Exception as e:
                resultados[exchange] = pd.Series(dtype=str)
                print(f"[{exchange}] Error al obtener precio: {e}")
    
        return resultados