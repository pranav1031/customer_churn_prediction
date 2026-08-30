from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load('../models/churn_model.pkl')
scaler = joblib.load('../models/scaler.pkl')

class CustomerData(BaseModel):
    gender: int
    SeniorCitizen: int
    Partner: int
    Dependents: int
    tenure: float
    PhoneService: int
    PaperlessBilling: int
    MonthlyCharges: float
    TotalCharges: float
    MultipleLines_No_phone_service: int
    MultipleLines_Yes: int
    InternetService_Fiber_optic: int
    InternetService_No: int
    OnlineSecurity_No_internet_service: int
    OnlineSecurity_Yes: int
    OnlineBackup_No_internet_service: int
    OnlineBackup_Yes: int
    DeviceProtection_No_internet_service: int
    DeviceProtection_Yes: int
    TechSupport_No_internet_service: int
    TechSupport_Yes: int
    StreamingTV_No_internet_service: int
    StreamingTV_Yes: int
    StreamingMovies_No_internet_service: int
    StreamingMovies_Yes: int
    Contract_One_year: int
    Contract_Two_year: int
    PaymentMethod_Credit_card_automatic: int
    PaymentMethod_Electronic_check: int
    PaymentMethod_Mailed_check: int


@app.get("/")
def home():
    return {"message": "Churn Prediction API is coming"}

@app.post("/predict")
def predict(data: CustomerData):
    input_df = pd.DataFrame([data.dict()])
    input_df.columns = [
        'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService',
        'PaperlessBilling', 'MonthlyCharges', 'TotalCharges',
        'MultipleLines_No phone service', 'MultipleLines_Yes',
        'InternetService_Fiber optic', 'InternetService_No',
        'OnlineSecurity_No internet service', 'OnlineSecurity_Yes',
        'OnlineBackup_No internet service', 'OnlineBackup_Yes',
        'DeviceProtection_No internet service', 'DeviceProtection_Yes',
        'TechSupport_No internet service', 'TechSupport_Yes',
        'StreamingTV_No internet service', 'StreamingTV_Yes',
        'StreamingMovies_No internet service', 'StreamingMovies_Yes',
        'Contract_One year', 'Contract_Two year',
        'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check',
        'PaymentMethod_Mailed check'
    ]

    num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    input_df[num_cols] = scaler.transform(input_df[num_cols])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    return {
        "churn_prediction": int(prediction),
        "churn_probability": round(float(probability), 4)
    }