# Bot IA Cripto – EstebanCryptoIA
import os
from pybit.unified_trading import HTTP
import time

API_KEY = os.getenv("BYBIT_API_KEY")
API_SECRET = os.getenv("BYBIT_API_SECRET")

session = HTTP(
    api_key=API_KEY,
    api_secret=API_SECRET,
)

def ejecutar_trade():
    try:
        balance = session.get_wallet_balance(accountType="UNIFIED")["result"]["list"][0]["coin"]
        usdt_balance = next((coin for coin in balance if coin["coin"] == "USDT"), None)

        if usdt_balance:
            print(f"✅ Bot activo. Balance disponible: {usdt_balance['availableToWithdraw']} USDT")
        else:
            print("⚠️ No se encontró USDT en la cuenta.")

    except Exception as e:
        print("❌ Error al conectarse con la API de Bybit:", e)

if __name__ == "__main__":
    while True:
        ejecutar_trade()
        time.sleep(30)  # Espera 30 segundos antes de repetir
