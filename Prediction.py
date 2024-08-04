import numpy as np
import streamlit as st
import pandas as pd
import pickle
import sklearn

with open('trained_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Insurance Premium Prediction")

# Input fields for the features
age = st.number_input('Age', min_value=0, max_value=100, value=25)
diabetes = st.selectbox('Diabetes', [0, 1])
blood_pressure_problems = st.selectbox('Blood Pressure Problems', [0, 1])
any_transplants = st.selectbox('Any Transplants', [0, 1])
any_chronic_diseases = st.selectbox('Any Chronic Diseases', [0, 1])
height = st.number_input('Height (cm)', min_value=50, max_value=250, value=170)
weight = st.number_input('Weight (kg)', min_value=10, max_value=300, value=70)
known_allergies = st.selectbox('Known Allergies', [0, 1])
history_of_cancer_in_family = st.selectbox('History of Cancer in Family', [0, 1])
number_of_major_surgeries = st.number_input('Number of Major Surgeries', min_value=0, max_value=10, value=0)
# BMI calculation
bmi = weight / (height / 100) ** 2

# Prepare the input data for prediction
input_data = pd.DataFrame({
    'Age': [age],
    'Diabetes': [diabetes],
    'BloodPressureProblems': [blood_pressure_problems],
    'AnyTransplants': [any_transplants],
    'AnyChronicDiseases': [any_chronic_diseases],
    'KnownAllergies': [known_allergies],
    'HistoryOfCancerInFamily': [history_of_cancer_in_family],
    'NumberOfMajorSurgeries': [number_of_major_surgeries],
    'BMI': [bmi]
})



# Predict the insurance premium
if st.button('Predict'):
    prediction = model.predict(input_data)
    st.write(f"Predicted Insurance Premium: ${prediction[0]:.2f}")




