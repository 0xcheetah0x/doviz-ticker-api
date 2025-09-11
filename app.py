from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import requests
import os

app = FastAPI()

# CORS ayarları
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
        # frankfurter API kullanıyoruz
        fx = requests.get("https://api.frankfurter.app/latest?from=USD&to=TRY,EUR,GBP,CHF,JPY").json()
        rates = fx["rates"]

        usdtry = round(rates["TRY"], 2)
        eurtry = round(rates["TRY"] / rates["EUR"], 2)
        gbptry = round(rates["TRY"] / rates["GBP"], 2)
        chftry = round(rates["TRY"] / rates["CHF"], 2)
        jpytry = round(rates["TRY"] / rates["JPY"], 2)

        return {
            "usdtry": usdtry,
            "eurtry": eurtry,
            "gbptry": gbptry,
            "chftry": chftry,
            "jpytry": jpytry
        }
    except Exception as e:
        return {"error": str(e)}

# doviz.html'i render et
@app.get("/doviz.html")
def serve_html():
    return FileResponse(os.path.join(os.path.dirname(__file__), "doviz.html"))
