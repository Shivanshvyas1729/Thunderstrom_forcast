import streamlit as st
import pandas as pd
import joblib
# for streamlit deployment
# -----------------------
# Load Model
# -----------------------
MODEL_PATH = "model/RandomForest_best_model.pkl"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

# -----------------------
# Feature Columns (Must Match Training EXACTLY)
# -----------------------
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

# -----------------------
# UI
# -----------------------
st.title("🌩 Weather Thunderstorm Prediction App")
st.write("Enter atmospheric parameters to predict Thunderstorm (TH)")

SWEAT_index = st.number_input("SWEAT index", value=0.0)
K_index = st.number_input("K index", value=0.0)
Totals_totals_index = st.number_input("Totals totals index", value=0.0)
Environmental_Stability = st.number_input("Environmental Stability", value=0.0)
Moisture_Indices = st.number_input("Moisture Indices", value=0.0)
Convective_Potential = st.number_input("Convective Potential", value=0.0)
Temperature_Pressure = st.number_input("Temperature Pressure", value=0.0)
Moisture_Temperature_Profiles = st.number_input("Moisture Temperature Profiles", value=0.0)

# -----------------------
# Prediction
# -----------------------
if st.button("Predict"):

    input_data = pd.DataFrame([[
        SWEAT_index,
        K_index,
        Totals_totals_index,
        Environmental_Stability,
        Moisture_Indices,
        Convective_Potential,
        Temperature_Pressure,
        Moisture_Temperature_Profiles
    ]], columns=FEATURE_COLUMNS)

    prediction = model.predict(input_data)[0]

    proba = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(input_data)[:, -1][0]

    st.success(f"Prediction: {int(prediction)}")

    if proba is not None:
        st.info(f"Probability: {proba:.4f}")

    # Optional interpretation
    if prediction == 1:
        st.error("⚠ Thunderstorm Likely")
    else:
        st.success("✅ No Thunderstorm Expected")