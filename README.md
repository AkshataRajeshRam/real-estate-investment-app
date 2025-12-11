# real-estate-investment-app
Machine Learning–powered web app that analyzes property features and predicts investment suitability. Includes preprocessing pipeline, Random Forest classifier, and Streamlit UI.

<img width="635" height="878" alt="image" src="https://github.com/user-attachments/assets/3735cdec-7c2e-4d19-b5f6-c010b4274bb9" />

----

📌 Overview

This project analyzes property features and predicts whether a real estate listing is a good investment using a trained Machine Learning model.
The app includes:

🧹 Automated preprocessing pipeline
🌲 Random Forest classifier
🖥️ Interactive Streamlit UI
📊 Real-time prediction based on user inputs

----

🚀 Features

✔ Predicts if a property is a Good Investment or Not Suitable
✔ Uses advanced ML techniques for better accuracy
✔ Easy-to-use web interface built with Streamlit
✔ Includes model, preprocessing steps, and all dependencies
✔ Takes features like:

State
City
Area size
Price per sq ft
Bathrooms, BHK
Furnishing details
Construction status
Property type

----

🧠 Machine Learning Model

Algorithm: Random Forest Classifier

Training: Cleaned and preprocessed dataset with one-hot encoding

Output: Binary classification — Suitable / Not Suitable

Model File: investment_classifier_model_compressed.pkl

----

📂 Project Structure
├── app.py                                # Streamlit frontend + prediction logic
├── investment_classifier_model_compressed.pkl  # Trained ML model
├── requirements.txt                       # Dependencies
└── README.md                              # Project documentation

----

▶️ How to Run the App Locally
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Run the Streamlit App
streamlit run app.py

The app will open in your browser at:
http://localhost:8501

----

🛠 Technologies Used

Python
Scikit-learn
Pandas
NumPy
Streamlit
Pickle for model storage

----

📈 Future Improvements

🔹 Add price prediction using regression
🔹 Visual analytics dashboard
🔹 Geolocation-based suggestions
🔹 Integration with real property listings
