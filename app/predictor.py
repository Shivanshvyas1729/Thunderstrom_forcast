import pandas as pd
from app.model_loader import model

FEATURE_COLUMNS = [
    "SWEAT index",
    "K index",
    "Totals totals index",
    "Environmental_Stability",
    "Moisture_Indices",
    "Convective_Potential",
    "Temperature_Pressure",
    "Moisture_Temperature_Profiles"
]

# logic to make prediction
def predict_weather(feature_dict: dict):

    # Ensure correct column order
    df = pd.DataFrame([feature_dict])
    df = df[FEATURE_COLUMNS]

    prediction = model.predict(df)

    proba = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(df)[:, -1][0]

    return {
        "prediction": int(prediction[0]),
        "probability": float(proba) if proba is not None else None
    }