from pydantic import BaseModel


class WeatherInput(BaseModel):
    SWEAT_index: float
    K_index: float
    Totals_totals_index: float
    Environmental_Stability: float
    Moisture_Indices: float
    Convective_Potential: float
    Temperature_Pressure: float
    Moisture_Temperature_Profiles: float

    # Convert API input → Training feature names
    def to_model_input(self):
        return {
            "SWEAT index": self.SWEAT_index,
            "K index": self.K_index,
            "Totals totals index": self.Totals_totals_index,
            "Environmental_Stability": self.Environmental_Stability,
            "Moisture_Indices": self.Moisture_Indices,
            "Convective_Potential": self.Convective_Potential,
            "Temperature_Pressure": self.Temperature_Pressure,
            "Moisture_Temperature_Profiles": self.Moisture_Temperature_Profiles
        }