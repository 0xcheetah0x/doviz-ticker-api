from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# CORS açıyoruz (OBS tarayıcı kaynağı rahat erişsin diye)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ana sayfa endpointi
@app.get("/")
def root():
    return {
        "message": "Doviz Ticker API çalışıyor 🚀",
        "endpoints": {
            "/api/doviz": "USD, EUR ve BTC bilgilerini getirir"
        }
    }

@app.get("/api/doviz")
def doviz():
    try:
        # USD & EUR verisi
        fx = requests.get("https://open.er-api.com/v6/latest/USD").json()
        usdtry = round(fx["rates"]["TRY"], 2)
        eurtry = round(fx["rates"]["TRY"] / fx["rates"]["EUR"], 2)

        # Bitcoin verisi
        btc = requests.get("https://api.coindesk.com/v1/bpi/currentprice/USD.json").json()
        btcusd = round(btc["bpi"]["USD"]["rate_float"], 0)

        return {
            "usdtry": usdtry,
            "eurtry": eurtry,
            "btcusd": btcusd
        }
    except Exception as e:
        return {"error": str(e)}
