import requests
import json

# Sample house data with correct column names
sample_data = {
    "Order": 1,
    "PID": 5286,
    "MS_SubClass": 20,
    "Lot_Frontage": 80.0,
    "Lot_Area": 9600,
    "Overall_Qual": 5,
    "Overall_Cond": 7,
    "Year_Built": 1961,
    "Year_Remod_Add": 1961,
    "Mas_Vnr_Area": 0.0,
    "BsmtFin_SF_1": 700.0,
    "BsmtFin_SF_2": 0.0,
    "Bsmt_Unf_SF": 150.0,
    "Total_Bsmt_SF": 850.0,
    "First_Flr_SF": 856,
    "Second_Flr_SF": 854,
    "Low_Qual_Fin_SF": 0,
    "Gr_Liv_Area": 1710.0,
    "Bsmt_Full_Bath": 5,
    "Bsmt_Half_Bath": 2,
    "Full_Bath": 1,
    "Half_Bath": 0,
    "Bedroom_AbvGr": 3,
    "Kitchen_AbvGr": 1,
    "TotRms_AbvGrd": 3,
    "Fireplaces": 2,
    "Garage_Yr_Blt": 1961,
    "Garage_Cars": 4,
    "Garage_Area": 500.0,
    "Wood_Deck_SF": 210.0,
    "Open_Porch_SF": 0,
    "Enclosed_Porch": 0,
    "Three_Ssn_Porch": 0,
    "Screen_Porch": 0,
    "Pool_Area": 0,
    "Misc_Val": 0,
    "Mo_Sold": 5,
    "Yr_Sold": 2010
}

# Make prediction request
response = requests.post(
    "http://localhost:8000/invocations",
    json=sample_data
)

# Print response
print("Prediction Response:")
print(json.dumps(response.json(), indent=2))
