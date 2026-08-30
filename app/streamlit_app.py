import streamlit as st
import requests

st.title("Customer Churn Predictor")

st.subheader("Customer Details")

gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", ["Yes","No"])
partner = st.selectbox("Has Partner", ["Yes", "No"])
dependents = st.selectbox("Has Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
total_charges = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])

if st.button("Predict Churn"):
    payload = {
        "gender": 1 if gender == "Male" else 0,
        "SeniorCitizen": 1 if senior == "Yes" else 0,
        "Partner": 1 if partner == "Yes" else 0,
        "Dependents": 1 if dependents == "Yes" else 0,
        "tenure": tenure,
        "PhoneService": 1 if phone_service == "Yes" else 0,
        "PaperlessBilling": 1 if paperless == "Yes" else 0,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "MultipleLines_No_phone_service": 0,
        "MultipleLines_Yes": 0,
        "InternetService_Fiber_optic": 1 if internet == "Fiber optic" else 0,
        "InternetService_No": 1 if internet == "No" else 0,
        "OnlineSecurity_No_internet_service": 1 if internet == "No" else 0,
        "OnlineSecurity_Yes": 0,
        "OnlineBackup_No_internet_service": 1 if internet == "No" else 0,
        "OnlineBackup_Yes": 0,
        "DeviceProtection_No_internet_service": 1 if internet == "No" else 0,
        "DeviceProtection_Yes": 0,
        "TechSupport_No_internet_service": 1 if internet == "No" else 0,
        "TechSupport_Yes": 0,
        "StreamingTV_No_internet_service": 1 if internet == "No" else 0,
        "StreamingTV_Yes": 0,
        "StreamingMovies_No_internet_service": 1 if internet == "No" else 0,
        "StreamingMovies_Yes": 0,
        "Contract_One_year": 1 if contract == "One year" else 0,
        "Contract_Two_year": 1 if contract == "Two year" else 0,
        "PaymentMethod_Credit_card_automatic": 1 if payment == "Credit card (automatic)" else 0,
        "PaymentMethod_Electronic_check": 1 if payment == "Electronic check" else 0,
        "PaymentMethod_Mailed_check": 1 if payment == "Mailed check" else 0,
    }


    response = requests.post("http://127.0.0.1:8000/predict", json=payload)
    result = response.json()

    st.subheader("Result")
    if result["churn_prediction"] == 1:
      st.error(f"Likely to churn - probability: {result['churn_probability']*100:.1f}%")
    else:
      st.success(f"Likely to stay - churn probability: {result['churn_probability']*100:.1f}%")