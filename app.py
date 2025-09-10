from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import requests
import os

app = FastAPI()

# CORS açıyoruz (OBS tarayıcı kaynağı rahat erişsin diye)
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
        # USD & EUR verisi
        fx = requests.get("https://open.er-api.com/v6/latest/USD").json()
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

# doviz.html'i render et
@app.get("/doviz.html")
def serve_html():
    return FileResponse(os.path.join(os.path.dirname(__file__), "doviz.html"))
