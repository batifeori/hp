import streamlit as st
import pandas as pd
import joblib

model = joblib.load("housing_price_model.pkl")

st.title("House Price Predictor")

area = st.number_input("Area", 500, 20000, 5000)
bedrooms = st.slider("Bedrooms",1,10,3)
bathrooms = st.slider("Bathrooms",1,5,2)
stories = st.slider("Stories",1,4,2)

mainroad = st.selectbox("Main Road",[0,1])
guestroom = st.selectbox("Guest Room",[0,1])
basement = st.selectbox("Basement",[0,1])
hotwaterheating = st.selectbox("Hot Water Heating",[0,1])
airconditioning = st.selectbox("Air Conditioning",[0,1])

parking = st.slider("Parking",0,3,1)
prefarea = st.selectbox("Preferred Area",[0,1])

furnishing = st.selectbox(
    "Furnishing Status",
    ["furnished","semi-furnished","unfurnished"]
)

# create base dictionary
data = {
    "area": area,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "stories": stories,
    "mainroad": mainroad,
    "guestroom": guestroom,
    "basement": basement,
    "hotwaterheating": hotwaterheating,
    "airconditioning": airconditioning,
    "parking": parking,
    "prefarea": prefarea,
    "furnishingstatus_semi-furnished": 0,
    "furnishingstatus_unfurnished": 0
}

# one-hot encode furnishing
if furnishing == "semi-furnished":
    data["furnishingstatus_semi-furnished"] = 1
elif furnishing == "unfurnished":
    data["furnishingstatus_unfurnished"] = 1

# create dataframe
input_df = pd.DataFrame([data])

# force column order to match model
input_df = input_df.reindex(columns=model.feature_names_in_)

if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted House Price: £{prediction:,.2f}")