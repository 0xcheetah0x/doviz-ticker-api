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

@app.get("/")
def root():
    return {"message": "Doviz Ticker API çalışıyor 🚀"}

@app.get("/api/doviz")
def doviz():
    try:
        # USD & EUR verisi
        fx = requests.get("https://open.er-api.com/v6/latest/USD").json()
        usdtry = round(fx["rates"]["TRY"], 2)
        eurtry = round(fx["rates"]["TRY"] / fx["rates"]["EUR"], 2)

        return {
            "usdtry": usdtry,
            "eurtry": eurtry
        }
    except Exception as e:
        return {"error": str(e)}

# doviz.html dosyasını servis et
@app.get("/doviz.html")
def get_html():
    return FileResponse(os.path.join(os.path.dirname(__file__), "doviz.html"))
