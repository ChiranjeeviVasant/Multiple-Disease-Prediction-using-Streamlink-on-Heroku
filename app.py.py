# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:06:51 2024

@author: Chiranjivi
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the models
diabetes_model = pickle.load(open('C:/Users/Chiranjivi/Desktop/Multiple Disease Prediction/saved models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/Chiranjivi/Desktop/Multiple Disease Prediction/saved models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('C:/Users/Chiranjivi/Desktop/Multiple Disease Prediction/saved models/parkinsons_model.sav', 'rb'))

# Set app theme color
st.markdown("""
    <style>
    .main {
        background-color: #2e2e2e;
        color: #e0e0e0;
    }
    .stTextInput > div > input {
        background-color: #555;
        color: white;
    }
    .stButton button {
        background-color: #3088ff;
        color: white;
        border-radius: 12px;
        padding: 10px 20px;
        border: 0;
        transition: background-color 0.3s;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    .css-1d391kg {
        background-color: #4A90E2;
    }
    .stSidebar {
        background-color: #1d1d1d;
    }
    .stSidebar > div > div {
        color: #e0e0e0;
    }
    </style>
    """, unsafe_allow_html=True)


# Sidebar navigation menu
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0,
                           styles={
                              "container": {"background-color": "#333"},
                              "nav-link": {"color": "white", "text-align": "center", "transition": "0.3s"},
                              "nav-link-selected": {"background-color": "#1E90FF"}
                           })

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.markdown("<h2 style='color: #ff4757;'>🩸 Diabetes Prediction Using ML</h2>", unsafe_allow_html=True)
   
    st.markdown("Enter the following details to check for **diabetes** prediction:")

    # Input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', placeholder="e.g., 2")

    with col2:
        Glucose = st.text_input('Glucose Level', placeholder="e.g., 120")

    with col3:
        BloodPressure = st.text_input('Blood Pressure value', placeholder="e.g., 70")

    with col1:
        SkinThickness = st.text_input('Skin Thickness value', placeholder="e.g., 30")

    with col2:
        Insulin = st.text_input('Insulin Level', placeholder="e.g., 80")

    with col3:
        BMI = st.text_input('BMI value', placeholder="e.g., 25.5")

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', placeholder="e.g., 0.45")

    with col2:
        Age = st.text_input('Age of the Person', placeholder="e.g., 50")

    diab_diagnosis = ''

    # Predict button
    if st.button('💉 Predict Diabetes'):
        try:
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                          BMI, DiabetesPedigreeFunction, Age]
            user_input = [float(x) for x in user_input]

            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 1:
                diab_diagnosis = '🟡 The person is diabetic.'
            else:
                diab_diagnosis = '🟢 The person is not diabetic.'
            
            st.success(diab_diagnosis)
        except Exception as e:
            st.error(f"Error: {e}")

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.markdown("<h2 style='color: #ff6347;'>❤️ Heart Disease Prediction Using ML</h2>", unsafe_allow_html=True)
    st.markdown("Enter the following details to check for **heart disease** prediction:")

    # Input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age', placeholder="e.g., 45")

    with col2:
        sex = st.text_input('Sex', placeholder="e.g., 1 for male, 0 for female")

    with col3:
        cp = st.text_input('Chest Pain types', placeholder="e.g., 2")

    with col1:
        trestbps = st.text_input('Resting Blood Pressure', placeholder="e.g., 130")

    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl', placeholder="e.g., 200")

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl', placeholder="e.g., 1")

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results', placeholder="e.g., 1")

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', placeholder="e.g., 150")

    with col3:
        exang = st.text_input('Exercise Induced Angina', placeholder="e.g., 0")

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise', placeholder="e.g., 2.3")

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment', placeholder="e.g., 1")

    with col3:
        ca = st.text_input('Major vessels colored by fluoroscopy', placeholder="e.g., 0")

    with col1:
        thal = st.text_input('Thal: 0 = normal, 1 = fixed defect, 2 = reversible defect', placeholder="e.g., 2")

    heart_diagnosis = ''

    # Predict button
    if st.button('🫀 Predict Heart Disease'):
        try:
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            user_input = [float(x) for x in user_input]

            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                heart_diagnosis = '🟡 The person has heart disease.'
            else:
                heart_diagnosis = '🟢 The person does not have heart disease.'
            
            st.success(heart_diagnosis)
        except Exception as e:
            st.error(f"Error: {e}")

if selected == "Parkinsons Prediction":
    st.markdown("<h2 style='color: #ffa500;'>🧠 Parkinson's Prediction Using ML</h2>", unsafe_allow_html=True)
    st.markdown("Enter the following details to check for **Parkinson's disease** prediction:")

    # Input fields grouped into 5 columns
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)', placeholder="e.g., 119.992")
        RAP = st.text_input('MDVP:RAP', placeholder="e.g., 0.00370")
        APQ3 = st.text_input('Shimmer:APQ3', placeholder="e.g., 0.00694")
        NHR = st.text_input('NHR', placeholder="e.g., 0.02211")
        spread1 = st.text_input('spread1', placeholder="e.g., -4.813031")

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)', placeholder="e.g., 157.302")
        PPQ = st.text_input('MDVP:PPQ', placeholder="e.g., 0.00554")
        APQ5 = st.text_input('Shimmer:APQ5', placeholder="e.g., 0.00908")
        HNR = st.text_input('HNR', placeholder="e.g., 21.033")
        spread2 = st.text_input('spread2', placeholder="e.g., 0.266482")

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)', placeholder="e.g., 74.997")
        DDP = st.text_input('Jitter:DDP', placeholder="e.g., 0.01210")
        APQ = st.text_input('MDVP:APQ', placeholder="e.g., 0.01029")
        RPDE = st.text_input('RPDE', placeholder="e.g., 0.414783")
        D2 = st.text_input('D2', placeholder="e.g., 2.423363")

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)', placeholder="e.g., 0.00784")
        Shimmer = st.text_input('MDVP:Shimmer', placeholder="e.g., 0.02079")
        DDA = st.text_input('Shimmer:DDA', placeholder="e.g., 0.03054")
        DFA = st.text_input('DFA', placeholder="e.g., 0.815285")
        PPE = st.text_input('PPE', placeholder="e.g., 0.220472")

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', placeholder="e.g., 0.00007")
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)', placeholder="e.g., 0.185")

    # Code for Prediction
    parkinsons_diagnosis = ''

    # Creating a button for Prediction
    if st.button("🧠 Predict Parkinson's Disease"):
        try:
            user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
            user_input = [float(x) for x in user_input]

            parkinsons_prediction = parkinsons_model.predict([user_input])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "🟡 The person has Parkinson's disease."
            else:
                parkinsons_diagnosis = "🟢 The person does not have Parkinson's disease."

            st.success(parkinsons_diagnosis)
        except Exception as e:
            st.error(f"Error: {e}")
