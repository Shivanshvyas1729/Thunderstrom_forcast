
# 🌦 Thunderstorm (TH) Forecasting System

[🚀 Live Demo](https://thunderstromforcast.streamlit.app/)

A machine learning–based application for **Thunderstorm (TH) occurrence prediction** using atmospheric indices.  
The project uses a **pre-trained & compressed Random Forest model** and provides an **interactive Streamlit web interface** for real-time predictions.

---

## 🚀 Features

- ✅ Pre-trained **Random Forest Classifier**
- ✅ Model optimized using **Joblib compression**
- ✅ Interactive **Streamlit UI**
- ✅ Inference-only (no retraining required)
- ✅ FastAPI backend support
- ✅ Ready for **Cloud Deployment (Streamlit Cloud / Render / AWS)**
- ✅ Modular & production-ready structure

---

## 📊 Input Features

The model predicts thunderstorm occurrence using the following atmospheric parameters:

- SWEAT Index  
- K Index  
- Totals Totals Index  
- Environmental Stability  
- Moisture Indices  
- Convective Potential  
- Temperature Pressure  
- Moisture Temperature Profiles  

---

## 🧠 Model Details

- **Algorithm**: Random Forest Classifier  
- **Training**: Performed offline using historical atmospheric datasets  
- **Class Imbalance Handling**: SMOTE  

### 📈 Evaluation Metrics

- Accuracy  
- Precision  
- Recall  
- F1-score  
- Probability of Detection (POD)  
- False Alarm Rate (FAR)  
- Heidke Skill Score (HSS)  
- Critical Success Index (CSI)  

- **Model Format**: `joblib`
- **Compressed Size**: ~5–10 MB  

---

## 🛠 Tech Stack

- Python  
- Scikit-learn  
- Imbalanced-learn  
- Pandas & NumPy  
- FastAPI  
- Streamlit  

---

## 📦 Project Structure

```

Thunderstrom_forcast/
│
├── api/
│   └── main.py              # FastAPI backend
│
├── streamlit_app/
│   └── ui/
│       └── streamlit.py     # Streamlit frontend
│
├── model/
│   └── RandomForest_best_model.pkl
│
├── requirements.txt
├── runtime.txt
└── README.md

````

---

# ▶️ Run Locally

## 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
````

---

## 2️⃣ Run FastAPI Backend

```bash
uvicorn api.main:app --reload
```

Backend will start at:

```
http://127.0.0.1:8000
```

Swagger API docs:

```
http://127.0.0.1:8000/docs
```

### Available Endpoints

* `GET /` → Health check
* `POST /predict` → Thunderstorm prediction

---

## 3️⃣ Run Streamlit Frontend

Open a new terminal and run:

```bash
streamlit run streamlit_app/ui/streamlit.py
```

Streamlit will open at:

```
http://localhost:8501
```

---

# ☁️ Deployment

The application is deployable on:

* Streamlit Cloud
* Render
* AWS
* Docker

---

## 📌 Note

This repository contains only the inference pipeline.
Model training and dataset preparation are performed offline.

---

## 📄 License

MIT
