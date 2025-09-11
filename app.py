from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import requests
import os

app = FastAPI()

# CORS (OBS tarayıcı kaynağı için)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API endpoint
@app.get("/api/doviz")
def doviz():
    try:
        # TRY bazlı çağırıyoruz
        url = "https://api.exchangerate.host/latest?base=TRY&symbols=USD,EUR,GBP,CHF,JPY"
        fx = requests.get(url).json()

        rates = fx.get("rates", {})

        # Büyük/küçük harf farkını normalize edelim
        rates = {k.upper(): v for k, v in rates.items()}

        usdtry = round(1 / rates["USD"], 2)
        eurtry = round(1 / rates["EUR"], 2)
        gbptry = round(1 / rates["GBP"], 2)
        chftry = round(1 / rates["CHF"], 2)
        jpytry = round(1 / rates["JPY"], 2)

        return {
            "usdtry": usdtry,
            "eurtry": eurtry,
            "gbptry": gbptry,
            "chftry": chftry,
            "jpytry": jpytry
        }
    except Exception as e:
        return {"error": str(e)}

# doviz.html render
@app.get("/doviz.html")
def serve_html():
    return FileResponse(os.path.join(os.path.dirname(__file__), "doviz.html"))
