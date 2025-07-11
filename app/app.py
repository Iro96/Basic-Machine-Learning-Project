import streamlit as st
import pandas as pd
import joblib
from app.utils import load_config, load_data, predict

# Load configuration
config = load_config("config.yaml")

# Load model and data
model = joblib.load(config['model_path'])
data = load_data(config['data_path'])

# Title
st.title(config['dashboard_title'])

# Display data
st.write("### Input Data")
st.dataframe(data.head())

# Make prediction
st.write("### Make Prediction")
if st.button("Predict"):
    predictions = predict(model, data)
    st.write("Predictions:")
    st.write(predictions)
