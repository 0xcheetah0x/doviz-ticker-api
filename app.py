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
        # ExchangeRate.host API
        url = "https://api.exchangerate.host/latest?base=USD&symbols=TRY,EUR,GBP,CHF,JPY"
        fx = requests.get(url).json()

        usdtry = round(fx["rates"]["TRY"], 2)
        eurtry = round(fx["rates"]["TRY"] / fx["rates"]["EUR"], 2)
        gbptry = round(fx["rates"]["TRY"] / fx["rates"]["GBP"], 2)
        chftry = round(fx["rates"]["TRY"] / fx["rates"]["CHF"], 2)
        jpytry = round(fx["rates"]["TRY"] / fx["rates"]["JPY"], 2)

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
