# -*- coding: utf-8 -*-
"""fastapi.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1r_Dfn-AI7g5Qp21aasRzNQrUcetp0gZX
"""

from google.colab import drive
drive.mount('/content/drive')

!pip install fastapi uvicorn nest-asyncio pyngrok

# Import necessary libraries
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import nest_asyncio
from pyngrok import ngrok
import uvicorn

# Set your ngrok authtoken
!ngrok authtoken 2l1Iclqz76aX7WmwkDAbL90EcGi_2Kkw2D2SZ65XP9Whxs8r9  # Replace YOUR_AUTHTOKEN_HERE with your actual ngrok authtoken

# Initialize the FastAPI app
app = FastAPI()

# Load the trained model from Google Drive
model_path = '/content/drive/MyDrive/Updated_Model/train_model.pkl'
model = joblib.load(model_path)

# Define the data model that will be sent to the API
class InsuranceData(BaseModel):
    age: float
    bmi: float
    children: int
    sex_male: int
    smoker_yes: int
    region_northwest: int
    region_southeast: int
    region_southwest: int

# Define the prediction endpoint
@app.post("/predict")
def predict(data: InsuranceData):
    # Convert input data into the format required by the model
    input_data = np.array([[
        data.age,
        data.bmi,
        data.children,
        data.sex_male,
        data.smoker_yes,
        data.region_northwest,
        data.region_southeast,
        data.region_southwest
    ]])

    # Make the prediction using the loaded model
    prediction = model.predict(input_data)

    # Return the prediction as a JSON response
    return {"prediction": prediction[0]}

# Set up the Colab environment
nest_asyncio.apply()

# Expose the FastAPI app using ngrok
public_url = ngrok.connect(8000)
print(f"Public URL: {public_url}")

# Run the FastAPI app with Uvicorn
uvicorn.run(app, host="0.0.0.0", port=8000)