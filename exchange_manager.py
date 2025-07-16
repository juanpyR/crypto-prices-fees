import pandas as pd

class ExchangeManager:
    def __init__(self, crypto_handler, exchanges_config):
        self.crypto_handler = crypto_handler
        self.exchanges_config = exchanges_config

    def mostrar_precios(self, moneda, textos, display_handler):
        display_handler.render_header(textos["header_precios"].format(moneda=moneda))
        precios = self.crypto_handler.obtener_precios_por_moneda(moneda, self.exchanges_config)

        for ex, df in precios.items():
            if df.empty:
                display_handler.render_warning(textos["mensaje_par_no_disp"].format(ex.title()))
            else:
                precio = df.iloc[0]
                logo_url = self.exchanges_config.get(ex, {}).get("logo_url", "")
                display_handler.render_precio_formateado(logo_url, ex.title(), precio)

    def mostrar_fees_unificadas(self, moneda, textos, display_handler):
        display_handler.render_header(textos["header_fees"].format(moneda=moneda))
        
        # Obtener todas las tablas de fees por exchange
        tablas_fees = {}
        for ex in self.exchanges_config:
            config = self.exchanges_config.get(ex, {})
            df_fees = self.crypto_handler.obtener_fees_exchanges(moneda, ex, config)
            if not df_fees.empty:
                tablas_fees[ex] = df_fees
            else:
                # Si no hay info, agregamos tabla vacía con columnas esperadas
                tablas_fees[ex] = pd.DataFrame(columns=["Network", f"{ex.title()} fee"])

        # Unificar tablas en una sola
        df_fees_unificada = self._unificar_fees_por_red(tablas_fees)

        display_handler.render_tabla_fees_unificada(df_fees_unificada)
        display_handler.render_minimos_por_exchange(df_fees_unificada,moneda, textos, formatear_func=self.crypto_handler.formatear_precio)

    def _unificar_fees_por_red(self, todas_las_tablas):
        # Construye tabla con filas = redes y columnas = exchanges
        df_unificado = pd.DataFrame()

        for ex, df in todas_las_tablas.items():
            if df.empty:
                continue
            # Renombrar columna de fees para que sea el nombre del exchange
            df_copy = df.copy()
            df_copy = df_copy.rename(columns={f"{ex.title()} fee": ex.title()})
            df_copy = df_copy.set_index("Network")

            if df_unificado.empty:
                df_unificado = df_copy
            else:
                df_unificado = df_unificado.join(df_copy, how="outer")

        # Rellenar valores NaN con '--' para indicar ausencia de info
        df_unificado = df_unificado.fillna("--")

        # Reordenar índices alfabéticamente para mejor lectura
        df_unificado = df_unificado.sort_index()

        # Resetear índice para mostrar la columna 'Network' normal
        df_unificado = df_unificado.reset_index()

        return df_unificado
