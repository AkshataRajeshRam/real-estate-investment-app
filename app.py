import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Real Estate Investment Advisor", page_icon="🏡")

# Load model
model = joblib.load("investment_classifier_model.pkl")

st.title("🏡 Real Estate Investment Advisor")
st.write("Fill the details below to check if the property is a Good Investment.")

state = st.text_input("State")
city = st.text_input("City")
locality = st.text_input("Locality")
property_type = st.selectbox("Property Type", ["Apartment", "Independent House", "Villa"])
bhk = st.number_input("BHK", 1, 10, 2)
size_sqft = st.number_input("Size in SqFt", 300, 12000, 1200)
price_per_sqft = st.number_input("Price per SqFt", 0.01, 1000.0, 0.10)
year_built = st.number_input("Year Built", 1950, 2024, 2010)
furnished_status = st.selectbox("Furnished Status", ["Furnished", "Unfurnished", "Semi-furnished"])
nearby_schools = st.number_input("Nearby Schools", 0, 50, 5)
nearby_hospitals = st.number_input("Nearby Hospitals", 0, 50, 3)
parking_space = st.number_input("Parking Space", 0, 5, 1)

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "State": state,
        "City": city,
        "Locality": locality,
        "Property_Type": property_type,
        "BHK": bhk,
        "Size_in_SqFt": size_sqft,
        "Price_per_SqFt": price_per_sqft,
        "Year_Built": year_built,
        "Furnished_Status": furnished_status,
        "Nearby_Schools": nearby_schools,
        "Nearby_Hospitals": nearby_hospitals,
        "Parking_Space": parking_space
    }])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("🏆 This is a GOOD INVESTMENT 🚀")
    else:
        st.error("⚠️ This property is NOT a good investment.")
