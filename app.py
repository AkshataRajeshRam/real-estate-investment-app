import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Real Estate Investment Advisor", page_icon="🏡")

# Load model
model = joblib.load("investment_classifier_model_compressed.pkl")

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

# Additional fields required by the model
infra_score = st.number_input("Infra Score", min_value=0.0, max_value=1.0, step=0.01)
amenities_count = st.number_input("Amenities Count", min_value=0, max_value=20, step=1)
owner_type = st.selectbox("Owner Type", ["Owner", "Builder", "Agent"])
availability_status = st.selectbox("Availability Status", ["Ready to Move", "Under Construction"])


if st.button("Predict"):

    input_data = pd.DataFrame([{
        "Price_per_SqFt": price_per_sqft,
        "Infra_Score": infra_score,
        "Amenities_Count": amenities_count,
        "Size_in_SqFt": size_sqft,
        "Nearby_Schools": nearby_schools,
        "Nearby_Hospitals": nearby_hospitals,
        "Parking_Space": parking_space,
        "Property_Type": property_type,
        "Furnished_Status": furnished_status,
        "Owner_Type": owner_type,
        "Availability_Status": availability_status,
        "State": state,
        "City": city
    }])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("🎉 This is a GOOD INVESTMENT 💹")
    else:
        st.error("⚠️ This property is NOT a good investment.")
