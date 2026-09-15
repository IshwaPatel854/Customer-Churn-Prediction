import streamlit as st
import pandas as pd
import joblib
import os

# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# Load model and preprocessor
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(
    os.path.join(BASE_DIR, "models", "logistic_regression_model.pkl")
)

preprocessor = joblib.load(
    os.path.join(BASE_DIR, "models", "preprocessor.pkl")
)

# --------------------------------------------------
# Custom styling
# --------------------------------------------------

st.markdown("""
<style>
    .main-title {
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 22px;
        font-weight: 600;
        margin-top: 15px;
        margin-bottom: 10px;
    }

    .info-box {
        padding: 18px;
        border-radius: 12px;
        background-color: #f3f6ff;
        border: 1px solid #d9e2ff;
        margin-bottom: 20px;
    }

    div.stButton > button {
        width: 100%;
        height: 50px;
        font-size: 18px;
        font-weight: 600;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="main-title">📊 Customer Churn Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict whether a customer is likely to discontinue the service '
    'using Machine Learning.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-box">
<b>How it works:</b><br>
Enter the customer's demographic, subscription, service and billing details.
The trained Logistic Regression model will predict the customer's churn risk.
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Customer Profile
# --------------------------------------------------

st.markdown(
    '<div class="section-title">👤 Customer Profile</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])

with col2:
    senior_citizen = st.selectbox("Senior Citizen", [0, 1])

with col3:
    partner = st.selectbox("Partner", ["Yes", "No"])

with col4:
    dependents = st.selectbox("Dependents", ["Yes", "No"])

# --------------------------------------------------
# Subscription Details
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📋 Subscription Details</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    tenure = st.number_input(
        "Tenure (months)",
        min_value=0,
        max_value=72,
        value=12
    )

with col2:
    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

with col3:
    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

with col4:
    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

# --------------------------------------------------
# Internet & Services
# --------------------------------------------------

st.markdown(
    '<div class="section-title">🌐 Internet & Services</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

with col2:
    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

with col3:
    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )

with col4:
    device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

col1, col2, col3, col4 = st.columns(4)

with col1:
    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

with col2:
    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

with col3:
    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

# --------------------------------------------------
# Billing Details
# --------------------------------------------------

st.markdown(
    '<div class="section-title">💳 Billing Details</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

with col2:
    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

with col3:
    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

with col4:
    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=840.0
    )

# --------------------------------------------------
# Prediction
# --------------------------------------------------

st.markdown("---")

if st.button("🔍 Predict Customer Churn"):

    customer_data = pd.DataFrame([{
        "customerID": "new_customer",
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }])

    customer_encoded = preprocessor.transform(customer_data)

    prediction = model.predict(customer_encoded)[0]

    if prediction == "Yes":
        st.error(
            "⚠️ Customer is likely to churn."
        )
        st.warning(
            "This customer may require additional retention attention."
        )

    else:
        st.success(
            "✅ Customer is unlikely to churn."
        )
        st.info(
            "This customer currently shows a lower likelihood of churn."
        )

st.markdown("---")

st.caption(
    "Customer Churn Prediction & Business Analytics | "
    "Machine Learning Project"
)