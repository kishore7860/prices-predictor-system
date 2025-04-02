from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import os

app = FastAPI()

# Load the trained model
MODEL_PATH = "model.joblib"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

model = joblib.load(MODEL_PATH)

class HouseData(BaseModel):
    Order: int
    PID: int
    MS_SubClass: int
    Lot_Frontage: float
    Lot_Area: int
    Overall_Qual: int
    Overall_Cond: int
    Year_Built: int
    Year_Remod_Add: int
    Mas_Vnr_Area: float
    BsmtFin_SF_1: float
    BsmtFin_SF_2: float
    Bsmt_Unf_SF: float
    Total_Bsmt_SF: float
    First_Flr_SF: int
    Second_Flr_SF: int
    Low_Qual_Fin_SF: int
    Gr_Liv_Area: float
    Bsmt_Full_Bath: int
    Bsmt_Half_Bath: int
    Full_Bath: int
    Half_Bath: int
    Bedroom_AbvGr: int
    Kitchen_AbvGr: int
    TotRms_AbvGrd: int
    Fireplaces: int
    Garage_Yr_Blt: int
    Garage_Cars: int
    Garage_Area: float
    Wood_Deck_SF: float
    Open_Porch_SF: int
    Enclosed_Porch: int
    Three_Ssn_Porch: int
    Screen_Porch: int
    Pool_Area: int
    Misc_Val: int
    Mo_Sold: int
    Yr_Sold: int

@app.post("/invocations")
async def predict(data: HouseData):
    try:
        # Convert input data to DataFrame with correct column names
        input_dict = data.dict()
        # Convert underscores to spaces in column names
        renamed_dict = {
            "MS_SubClass": "MS SubClass",
            "Lot_Frontage": "Lot Frontage",
            "Lot_Area": "Lot Area",
            "Overall_Qual": "Overall Qual",
            "Overall_Cond": "Overall Cond",
            "Year_Built": "Year Built",
            "Year_Remod_Add": "Year Remod/Add",
            "Mas_Vnr_Area": "Mas Vnr Area",
            "BsmtFin_SF_1": "BsmtFin SF 1",
            "BsmtFin_SF_2": "BsmtFin SF 2",
            "Bsmt_Unf_SF": "Bsmt Unf SF",
            "Total_Bsmt_SF": "Total Bsmt SF",
            "First_Flr_SF": "1st Flr SF",
            "Second_Flr_SF": "2nd Flr SF",
            "Low_Qual_Fin_SF": "Low Qual Fin SF",
            "Gr_Liv_Area": "Gr Liv Area",
            "Bsmt_Full_Bath": "Bsmt Full Bath",
            "Bsmt_Half_Bath": "Bsmt Half Bath",
            "Full_Bath": "Full Bath",
            "Half_Bath": "Half Bath",
            "Bedroom_AbvGr": "Bedroom AbvGr",
            "Kitchen_AbvGr": "Kitchen AbvGr",
            "TotRms_AbvGrd": "TotRms AbvGrd",
            "Garage_Yr_Blt": "Garage Yr Blt",
            "Garage_Cars": "Garage Cars",
            "Garage_Area": "Garage Area",
            "Wood_Deck_SF": "Wood Deck SF",
            "Open_Porch_SF": "Open Porch SF",
            "Enclosed_Porch": "Enclosed Porch",
            "Three_Ssn_Porch": "3Ssn Porch",
            "Screen_Porch": "Screen Porch",
            "Pool_Area": "Pool Area",
            "Misc_Val": "Misc Val",
            "Mo_Sold": "Mo Sold",
            "Yr_Sold": "Yr Sold"
        }
        
        # Rename the keys in the dictionary
        for old_key, new_key in renamed_dict.items():
            if old_key in input_dict:
                input_dict[new_key] = input_dict.pop(old_key)
                
        input_data = pd.DataFrame([input_dict])
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        
        return {"predicted_price": float(prediction)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 