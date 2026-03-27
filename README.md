# 📰 Fake News Detection AI (Hybrid ML + LLM)

An intelligent fake news detection system that combines **Machine Learning** and **LLM-based fact checking** to analyze and verify news content.

---

## 🚀 Features

* 🧠 **Machine Learning Model**

  * Logistic Regression with TF-IDF
  * Detects fake vs real news patterns

* 🤖 **LLM Fact Checking (Ollama - LLaMA3)**

  * Verifies real-world claims
  * Provides reasoning-based output

* ⚡ **Hybrid Decision System**

  * LLM for real-world facts
  * ML as fallback

* 📊 **Confidence Score + Visual Bar**

  * Displays prediction confidence
  * Interactive UI feedback

* 🎨 **Premium Frontend UI**

  * Glassmorphism design
  * Smooth animations
  * Clean user experience

---

## 🧠 System Architecture

```
User Input
   ↓
Frontend (HTML/CSS/JS)
   ↓
FastAPI Backend
   ↓
[ ML Model ] + [ LLM (Ollama) ]
   ↓
Final Prediction + Fact Check
```

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Frontend:** HTML, CSS, JavaScript
* **ML:** Scikit-learn (TF-IDF + Logistic Regression)
* **LLM:** Ollama (LLaMA3)
* **Tools:** Python, Git, GitHub

---

## 📂 Project Structure

```
Fake-news-detection/
│
├── backend/
│   ├── main.py
│   ├── model.py
│   ├── preprocess.py
│   └── train.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── data/ (ignored in repo)
├── model/ (ignored in repo)
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone repository

```bash
git clone https://github.com/Diya782/fake-news-detection.git
cd fake-news-detection
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r backend/requirements.txt
```

---

### 4️⃣ Run backend

```bash
cd backend
uvicorn main:app --reload --port 8001
```

---

### 5️⃣ Run frontend

Open:

```
frontend/index.html
```

---

### 6️⃣ Run Ollama (for fact checking)

```bash
ollama run llama3
```

---

## 🧪 Example Inputs

* `IPL 2026 starts on 28th March`
* `Aliens landed in Delhi yesterday`
* `Government announces new policy`

---

## ⚠️ Limitations

* ML model is trained on historical data (pattern-based)
* LLM does not have real-time internet access
* Accuracy depends on input quality and context

---

## 🌟 Future Improvements

* 🌐 Real-time news API integration
* 📊 Advanced model (PassiveAggressive / BERT)
* 📱 Fully responsive UI
* ☁️ Deployment (Render / Vercel)

---

## 👩‍💻 Author

**Diya Manth**
GitHub: https://github.com/Diya782


