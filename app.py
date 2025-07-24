import streamlit as st 
import numpy as np 
import joblib as jb
import pandas as pd

model = jb.load('Logistic_regression_heart.pkl')
scaler = jb.load('scaler.pkl')
expected_columns = jb.load('columns.pkl')

st.title('Heart Stroke Prediction App 💖')
st.subheader('Provide the following details.')

age = st.slider('Age', 18, 100, 40)
gender = st.selectbox("Gender", ['M', 'F'])
chest_pain_type = st.selectbox('Chest Pain Type', ['ATA', 'NAP', 'ASY', 'TA'])
resting_bp = st.number_input('Resting Blood Pressure (mm Hg)', 80, 200)
cholestrol = st.number_input('Cholestrol (mg/dl)', 100, 600, 200)
fasting_bs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0,1])
resting_ecg = st.selectbox('Resting Electrocardiographic', ['Normal', 'LVH', 'ST'])
max_hr = st.number_input('Maximum heart Rate', 60, 220, 150)
exercise_angina = st.selectbox('Exercise-Induced Angina', ['Yes', 'No'])
old_peak = st.number_input('OldPeak (ST Depression)', 0.0, 10.0, 1.0)
st_slope = st.selectbox('Slope of ST segment', ['Up', 'Flat', 'Down'])
if st.button('Predict'):
    raw_input = {
        'Age': age,
        'Sex': gender,
        'ChestPainType_' + chest_pain_type: 1,
        'RestingBP': resting_bp,
        'Cholesterol': cholestrol,
        'FastingBS': fasting_bs,
        'RestingECG_' + resting_ecg: 1,
        'MaxHR': max_hr,
        'ExerciseAngina' + exercise_angina: 1,
        'Oldpeak': old_peak,
        'ST_Slope_' + st_slope: 1 
    }
    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    if(prediction == 1):
        st.error('⚠️ High Risk of Heart Disease')
    else:
        st.success('✅ Low Risk of Heart Disease')