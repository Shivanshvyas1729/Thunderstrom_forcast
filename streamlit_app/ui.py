import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("Weather Thunderstorm Prediction App")
st.write("Enter atmospheric parameters to predict Thunderstorm (TH)")

# Inputs (ONLY 8 — match backend exactly)
SWEAT_index = st.number_input("SWEAT index", value=0.0)
K_index = st.number_input("K index", value=0.0)
Totals_totals_index = st.number_input("Totals totals index", value=0.0)
Environmental_Stability = st.number_input("Environmental Stability", value=0.0)
Moisture_Indices = st.number_input("Moisture Indices", value=0.0)
Convective_Potential = st.number_input("Convective Potential", value=0.0)
Temperature_Pressure = st.number_input("Temperature Pressure", value=0.0)
Moisture_Temperature_Profiles = st.number_input("Moisture Temperature Profiles", value=0.0)

if st.button("Predict"):

    payload = {
        "SWEAT_index": SWEAT_index,
        "K_index": K_index,
        "Totals_totals_index": Totals_totals_index,
        "Environmental_Stability": Environmental_Stability,
        "Moisture_Indices": Moisture_Indices,
        "Convective_Potential": Convective_Potential,
        "Temperature_Pressure": Temperature_Pressure,
        "Moisture_Temperature_Profiles": Moisture_Temperature_Profiles
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()

            st.success(f"Prediction: {result['prediction']}")
            
            if result["probability"] is not None:
                st.info(f"Probability: {result['probability']:.4f}")

        else:
            st.error(f"API Error: {response.text}")

    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to FastAPI backend. Is it running?")