
import streamlit as st
import pickle
import pandas as pd

# Load full pipeline (model + preprocessing)
with open("full_model_pipeline.pkl", "rb") as f:
    model_pipeline = pickle.load(f)

st.title("🚚 Food Delivery Time Prediction")

# User inputs
Distance_km = st.number_input("Distance (km)", min_value=0.0)
Vehicle_Type = st.selectbox("Vehicle Type", ["Bike", "Car", "Scooter"])
Time_of_Day = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
Courier_Experience_yrs = st.number_input("Courier Experience (yrs)", min_value=0)
Weather = st.selectbox("Weather", ["Clear", "Rainy", "Cloudy", "Stormy"])
Traffic_Level = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
Preparation_Time_min = st.number_input("Preparation Time (min)", min_value=0)

# Create dataframe for prediction
input_data = pd.DataFrame({
    "Distance_km": [Distance_km],
    "Vehicle_Type": [Vehicle_Type],
    "Time_of_Day": [Time_of_Day],
    "Courier_Experience_yrs": [Courier_Experience_yrs],
    "Weather": [Weather],
    "Traffic_Level": [Traffic_Level],
    "Preparation_Time_min": [Preparation_Time_min]
})

if st.button("Predict Delivery Time"):
    try:
        prediction = model_pipeline.predict(input_data)
        st.success(f"Estimated Delivery Time: {prediction[0]:.2f} minutes")
    except Exception as e:
        st.error(f"❌ Prediction error: {e}")
