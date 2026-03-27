from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from model import predict_news

app = FastAPI()

# ✅ CORS FIX (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NewsInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Fake News Detection API is running 🚀"}

@app.post("/predict")
def predict(data: NewsInput):
    result = predict_news(data.text)
    return {
        "prediction": result,
        "note": "⚠️ This model uses ML patterns, not real-time fact verification"
    }