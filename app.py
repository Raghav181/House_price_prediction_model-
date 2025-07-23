import streamlit as st
import pickle
import pandas as pd

# Load your model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🏠 House Price Prediction App")

area = st.number_input("Area (sqft)", 500, 5000, 1500)
bedrooms = st.number_input("Bedrooms", 1, 10, 3)
bathrooms = st.number_input("Bathrooms", 1, 10, 2)

features = pd.DataFrame([[area, bedrooms, bathrooms]], columns=['area', 'bedrooms', 'bathrooms'])

if st.button("Predict"):
    prediction = model.predict(features)
    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")
