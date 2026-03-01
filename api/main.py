# backend

from fastapi import FastAPI 
from app.schemas import WeatherInput 

from app.predictor import predict_weather


app = FastAPI(title= "Thunderstrome Prediction API")

#To ensure app is running 

@app.get("/")
def home():
    return {"message": "Weather Prediction API is running"}

#microsevice

@app.post("/predict")
def predict(data: WeatherInput):
    features = data.to_model_input()
    
    result = predict_weather(features)
    
    return result