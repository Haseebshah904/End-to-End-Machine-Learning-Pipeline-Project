# End-to-End-Machine-Learning-Pipeline-Project
This repository contains the code for an end-to-end machine learning pipeline, including data cleaning, model building, model saving and loading, FastAPI endpoint creation, and deployment on Hugging Face with a simple UI using Gradio or Streamlit.
# Project Structure

The project is organized into separate folders for each part of the assignment:

 Data_cleaning: Contains the script for data cleaning and preprocessing.

 Model train: Contains the script for building and evaluating the machine learning model.
 
 Model saving and loading: Contains the script for saving and loading the trained model.
 
 Api: Contains the script for creating the FastAPI application and prediction endpoint.

 App: Contains the script for creating the Gradio file and  deployment instructions.

# Prerequisites
Python 3.7 or higher

Required libraries: pandas, scikit-learn, joblib, fastapi, uvicorn, gradio

An account on Hugging Face

#Installation

Clone the repository:

bash

https://github.com/Haseebshah904/End-to-End-Machine-Learning-Pipeline-Project.git

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the required libraries:
bash
pip install -r requirements.txt

# Usage
# Data Cleaning:
Navigate to the data_cleaning folder.

Run the data_clean.py script to clean the dataset and save the cleaned data to a CSV file.

# Model Building:
Navigate to the model_building folder.

Run the model_train.py script to build and evaluate the machine learning model.

# Model Saving and Loading:
Navigate to the model_io folder.

The model_io.py script contains functions to save and load the trained model.

# FastAPI Endpoint:

Navigate to the api folder.

Run the fastapi.py script to start the FastAPI application and prediction endpoint.

# Deployment on Hugging Face:

Navigate to the app folder.

Run the app.py and requirements.txt file to start the Gradio or Streamlit application.

Follow the instructions provided in the app folder to deploy the application on Hugging Face Spaces.

# Contributing

If you find any issues or have suggestions for improvements, feel free to create a new issue or submit a pull request.
