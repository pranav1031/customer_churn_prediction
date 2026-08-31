# Customer Churn Prediction

An end-to-end machine learning project that predicts whether a telecom customer is likely to churn, served through a FastAPI backend and a Streamlit web app.

## Problem Statement

Customer churn — when a customer stops using a company's service — is costly for subscription-based businesses. Identifying customers at risk of churning ahead of time lets a business intervene (offers, support, retention campaigns) before losing them. This project builds a model to predict churn probability from customer account and service data.

## Dataset

[Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) (IBM sample dataset) — 7,043 customers, 21 features covering demographics, account information, and subscribed services.

## Approach

1. **EDA** — analyzed churn distribution (~26.5% churn, imbalanced) and identified key churn drivers: contract type, tenure, and internet service type.
2. **Feature Engineering** — handled missing values in `TotalCharges`, encoded binary and multi-category categorical variables, scaled numerical features with `StandardScaler`.
3. **Modeling** — compared Logistic Regression and Random Forest, with and without class balancing, evaluated on precision, recall, F1, and ROC-AUC (accuracy alone is misleading on imbalanced data).
4. **Model Selection** — chose **Logistic Regression with `class_weight='balanced'`**, prioritizing recall on churners (catches 78% of actual churners) since missing a churner is costlier than a false alarm in this business context.
5. **Deployment** — wrapped the trained model in a FastAPI `/predict` endpoint and built a Streamlit UI for interactive predictions.

## Results

| Model | Recall (Churn) | Precision (Churn) | ROC-AUC |
|---|---|---|---|
| Logistic Regression | 0.56 | 0.66 | 0.842 |
| Random Forest | 0.48 | 0.62 | 0.823 |
| Random Forest (balanced) | 0.49 | 0.64 | 0.828 |
| **Logistic Regression (balanced)** | **0.78** | 0.51 | **0.842** |

## Key Churn Drivers

- **Contract type**: Month-to-month customers churn at 42.7% vs. 2.8% for two-year contracts
- **Tenure**: Churned customers average 18 months tenure vs. 37.5 months for retained customers
- **Internet service**: Fiber optic customers churn at 41.9% vs. 18.9% for DSL

## Tech Stack

- **ML**: Python, pandas, scikit-learn
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Model persistence**: joblib

## Project Structure

```
churn-project/
├── data/raw/               # dataset
├── notebooks/
│   ├── 01_eda.ipynb         # exploratory data analysis
│   └── 02_modeling.ipynb    # feature engineering + model training
├── api/
│   └── main.py              # FastAPI backend
├── app/
│   └── streamlit_app.py     # Streamlit frontend
├── models/                  # saved model + scaler
├── requirements.txt
└── README.md
```

## Running Locally

```bash
# install dependencies
pip install -r requirements.txt

# start the API
cd api
uvicorn main:app --reload

# in a new terminal, start the frontend
cd app
streamlit run streamlit_app.py
```

## Future Improvements

- Hyperparameter tuning (GridSearchCV/Optuna)
- Try XGBoost/LightGBM with proper tuning
- SHAP values for model explainability
- Dockerize and deploy to a cloud platform

## Author

- Pranav Sharma