import streamlit as st
import pandas as pd
import joblib

model = joblib.load("housing_price_model.pkl")

st.title("House Price Predictor")

area = st.number_input("Area")
bedrooms = st.slider("Bedrooms",1,10,3)
bathrooms = st.slider("Bathrooms",1,5,2)
stories = st.slider("Stories",1,4,2)

mainroad = st.selectbox("Main Road",["yes","no"])
guestroom = st.selectbox("Guest Room",["yes","no"])
basement = st.selectbox("Basement",["yes","no"])
hotwaterheating = st.selectbox("Hot Water Heating",["yes","no"])
airconditioning = st.selectbox("Air Conditioning",["yes","no"])

parking = st.slider("Parking",0,3,1)
prefarea = st.selectbox("Preferred Area",["yes","no"])

furnishingstatus = st.selectbox(
    "Furnishing Status",
    ["furnished","semi-furnished","unfurnished"]
)

input_df = pd.DataFrame([[area,bedrooms,bathrooms,stories,
mainroad,guestroom,basement,hotwaterheating,airconditioning,
parking,prefarea,furnishingstatus]],

columns=['area','bedrooms','bathrooms','stories','mainroad',
'guestroom','basement','hotwaterheating','airconditioning',
'parking','prefarea','furnishingstatus'])

if st.button("Predict Price"):

    prediction = model.predict(input_df)[0]

    st.success(f"Predicted Price: {prediction:,.2f}")