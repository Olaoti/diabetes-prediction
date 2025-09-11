
import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🧑‍⚕️",
    layout="centered"
)

@st.cache_resource()
def load_model():
    model= joblib.load("diabetes_model.pkl")
    return model
model =load_model()

st.title("Welcome to Predia")
st.header("A place to predict your diabetes status ✅")
st.write("Kindly note that this is not an alternative to hospital diagnosis, Visit an hospital if you are not sure about your health")
st.divider()

gender = st.radio("Select a gender:",["Male","Female"])
age = st.number_input("Enter your Age",min_value=0, max_value=110)
urea = st.number_input("Enter Your Urea Level in mmol/L",min_value=0.0, max_value=14.0, step=0.1)
creatine = st.number_input("Enter Your Creatine Level in Umol/L",min_value=0, max_value=100)
HbA1c = st.number_input("Enter Your Average Blood Glucose in mmol/L", min_value=0.0, max_value=100.0, step=0.1)
Chol = st.number_input("Enter Your Cholesterol level in mmol/L", min_value=0.0, max_value=10.0, step=0.1)
Tg = st.number_input("Enter Your Triglycerides level in mmol/L", min_value=0.0, max_value=8.0, step=0.1)
Hdl = st.number_input("Enter Your HDL Cholesteron level in mmol/L",min_value=0.0, max_value=6.0, step=0.1)
Ldl = st.number_input("Enter Your LDL Cholesteron level in mmol/L",min_value=0.0, max_value=6.0, step=0.1)
Vldl = st.number_input("Enter Your VLDL Cholesteron level in mmol/L", min_value=0.0, max_value=35.0, step=0.1)
height = st.number_input("Enter Your Height in cm", min_value=5, max_value=250)
weight = st.number_input("Enter Your Weight in kg", min_value=1, max_value=200)


predict = st.button("Predict Diabetes")

gender_map={
    "Male":0,
    "Female":1,
}
prediction_map={
    0:"Congratulations! We do not think you are diabetic",
    1:"You might be diabetic, you should check with a doctor",
    2:"We think you are diabetic, That's not the end of the world. Please see a doctor "
}

if predict:
    data={
        "Gender":[gender_map.get(gender)],
        "AGE":[age],
        "Urea":[urea],
        "Cr":[creatine],
        "HbA1c":[HbA1c],
        "Chol":[Chol],
        "TG":[Tg],
        "HDL":[Hdl],
        "LDL":[Ldl],
        "VLDL":[Vldl],
        "BMI":[weight/(height/100)**2]
    }
    input_df = pd.DataFrame(data)
    prediction = model.predict(input_df)[0][0]
    proba = model.predict_proba(input_df)[0].max()
    prob=model.predict_proba(input_df)
    print(prob)
    if(prediction==0):
        st.success(prediction_map.get(prediction))
    else:
        st.error(prediction_map.get(prediction))
    st.write(f"This model is {proba*100:.1f}% sure of this answer")






