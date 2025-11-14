import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

st.set_page_config(page_title="Concrete Strength Prediction", layout="centered")

st.title("🧱 Concrete Compressive Strength Prediction App")
st.write("Enter the concrete mixture values to predict compressive strength (MPa).")

# Input fields
cement = st.number_input("Cement (kg/m³)", min_value=0.0)
slag = st.number_input("Blast Furnace Slag (kg/m³)", min_value=0.0)
flyash = st.number_input("Fly Ash (kg/m³)", min_value=0.0)
water = st.number_input("Water (kg/m³)", min_value=0.0)
superplasticizer = st.number_input("Superplasticizer (kg/m³)", min_value=0.0)
coarse_agg = st.number_input("Coarse Aggregate (kg/m³)", min_value=0.0)
fine_agg = st.number_input("Fine Aggregate (kg/m³)", min_value=0.0)
age = st.number_input("Age (days)", min_value=0.0)

# Prediction button
if st.button("Predict Strength"):
    input_data = pd.DataFrame([[
        cement, slag, flyash, water, superplasticizer,
        coarse_agg, fine_agg, age
    ]], columns=[
        "Cement", "Blast_Furnace_Slag", "Fly_Ash", "Water",
        "Superplasticizer", "Coarse_Aggregate", "Fine_Aggregate", "Age"
    ])

    result = model.predict(input_data)[0]
    st.success(f"Predicted Concrete Compressive Strength: *{result:.2f} MPa*")
