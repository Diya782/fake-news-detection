import pickle
import requests
from preprocess import preprocess

# Load ML model
model = pickle.load(open("../model/model.pkl", "rb"))
vectorizer = pickle.load(open("../model/vectorizer.pkl", "rb"))

# 🔥 LLM FACT CHECK (Ollama)
def verify_with_llm(text):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": f"Answer strictly in this format:\nTrue or False + short reason.\n\nStatement: {text}",
                "stream": False
            }
        )
        return response.json()["response"]
    except:
        return "⚠️ LLM not available"

# 🧠 ML prediction
def ml_prediction(text):
    cleaned = preprocess(text)
    vector = vectorizer.transform([cleaned])

    prob = model.predict_proba(vector)[0]
    confidence = max(prob)

    result = model.predict(vector)[0]
    label = "Fake ❌" if result == 0 else "Real ✅"

    return label, confidence

# 🚀 FINAL FUNCTION
def predict_news(text):
    llm_result = verify_with_llm(text)

    # 🔥 LLM takes priority
    if "Verdict: True" in llm_result:
        return f"Real ✅ (LLM Verified)\n\n🧠 {llm_result}"

    elif "Verdict: False" in llm_result:
        return f"Fake ❌ (LLM Verified)\n\n🧠 {llm_result}"

    elif "Not Verifiable" in llm_result:
        # fallback to ML
        label, confidence = ml_prediction(text)
        return f"{label} ({confidence*100:.2f}%)\n\n🧠 {llm_result}"

    return f"⚠️ Unable to determine\n\n{llm_result}"