# Customer Churn Prediction & Business Analytics using Machine Learning

## 1. Project Overview

Customer churn refers to customers discontinuing a company's services. Predicting churn helps businesses identify customers who are likely to leave and take preventive actions.

This project develops a complete machine learning and business analytics solution to analyze customer behavior, identify factors influencing churn, predict potential customer churn, and present the findings through an interactive dashboard and prediction application.

---

## 2. Objectives

The main objectives of this project are:

- Analyze customer behavior and churn patterns.
- Clean and preprocess customer data.
- Perform Exploratory Data Analysis (EDA).
- Identify important factors affecting customer churn.
- Perform feature engineering and feature selection.
- Develop machine learning models for churn prediction.
- Compare different machine learning algorithms.
- Evaluate model performance.
- Identify important churn-related features.
- Generate useful business insights.
- Create an interactive Power BI dashboard.
- Develop a Streamlit-based customer churn prediction interface.

---

## 3. Dataset

The project uses the **Telco Customer Churn dataset**.

The dataset contains information about:

- Customer demographics
- Customer tenure
- Phone services
- Internet services
- Online security and backup services
- Device protection
- Technical support
- Streaming services
- Contract type
- Payment method
- Monthly charges
- Total charges
- Customer churn status

The original dataset contained **7,043 customer records** and **21 columns**.

After converting `TotalCharges` from text to numeric values, 11 records with missing values were removed.

The final cleaned dataset contains **7,032 customer records**.

---

## 4. Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the customer churn dataset using Pandas.
2. Inspected the dataset using `head()` and `info()`.
3. Checked for missing values.
4. Converted `TotalCharges` from object/string type to numeric type.
5. Removed records with missing `TotalCharges`.
6. Separated the target variable `Churn`.
7. Converted categorical variables into numerical features using encoding.
8. Removed `customerID` from the machine learning feature set.
9. Split the dataset into training and testing sets using an 80:20 ratio.

---

## 5. Exploratory Data Analysis

EDA was performed to understand customer behavior and identify churn patterns.

### Churn Distribution

- Customers who did not churn: **73.42%**
- Customers who churned: **26.58%**

### Important Churn Patterns

#### Senior Citizens

Senior citizens showed a higher churn rate than non-senior customers.

#### Tenure

Customers with shorter tenure were more likely to churn.

The churn rate was highest among customers with **0–12 months of tenure** and decreased as customer tenure increased.

#### Contract Type

Month-to-month customers had the highest churn rate at approximately **42.71%**.

One-year contracts had a churn rate of approximately **11.28%**, while two-year contracts had a churn rate of approximately **2.85%**.

#### Monthly Charges

Customers who churned had a higher average monthly charge:

- Non-churned customers: approximately **61.31**
- Churned customers: approximately **74.44**

#### Payment Method

Customers using **Electronic Check** had a much higher churn rate than customers using automatic payment methods.

#### Internet Service

Fiber optic customers showed a higher churn rate than DSL customers.

#### Additional Services

Customers without services such as Online Security and Tech Support showed higher churn rates.

---

## 6. Feature Engineering

A `TenureGroup` feature was created to group customers according to their tenure:

- 0–12 months
- 13–24 months
- 25–36 months
- 37–48 months
- 49–60 months
- 61–72 months

Monthly charges were also grouped in the Power BI dashboard into:

- Under $30
- $30–$49
- $50–$69
- $70–$89
- $90–$109
- $110+

These groups make customer behavior easier to analyze and visualize.

---

## 7. Feature Selection

Feature selection was performed using the **SelectKBest** method with the ANOVA F-test.

The 15 selected features were:

1. tenure
2. MonthlyCharges
3. TotalCharges
4. InternetService_Fiber optic
5. InternetService_No
6. OnlineSecurity_No internet service
7. OnlineBackup_No internet service
8. DeviceProtection_No internet service
9. TechSupport_No internet service
10. StreamingTV_No internet service
11. StreamingMovies_No internet service
12. Contract_Two year
13. PaperlessBilling_Yes
14. PaymentMethod_Electronic check
15. TenureGroup_61-72 months

The selected features were saved in:

`models/selected_features.csv`

---

## 8. Machine Learning Models

Four machine learning algorithms were developed and compared:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

The dataset was divided into:

- **80% training data**
- **20% testing data**

---

## 9. Model Comparison

The models were compared using accuracy.

| Model | Accuracy |
|---|---:|
| Logistic Regression | 80.38% |
| Decision Tree | 78.96% |
| Random Forest | 75.27% |
| XGBoost | 79.74% |

### Best Performing Model

**Logistic Regression** achieved the highest accuracy of approximately **80.38%** among the four tested models.

The trained Logistic Regression model was saved for use in the Streamlit prediction application.

---

## 10. Model Evaluation

Model performance was evaluated using classification metrics including:

- Accuracy
- Precision
- Recall
- F1-score

These metrics help measure how effectively the model identifies customers who are likely to churn.

---

## 11. Feature Importance

Feature importance analysis was performed to identify factors that have a strong influence on churn prediction.

Important churn-related factors included:

- Month-to-month contracts
- Two-year contracts
- Fiber optic internet service
- Electronic check payment method
- Senior citizen status
- Online security
- Technical support
- Customer tenure

The analysis showed that contract type and customer tenure are particularly important factors related to churn.

---

## 12. Business Insights

The analysis provides the following business insights:

1. **Month-to-month customers are at higher risk of churn.**  
   Businesses can encourage customers to move to longer-term contracts.

2. **New customers are more likely to churn.**  
   Strong onboarding and early customer engagement can help improve retention.

3. **Higher monthly charges are associated with increased churn.**  
   Businesses can review pricing and provide suitable plans or offers.

4. **Electronic check users have a higher churn rate.**  
   Encouraging automatic payment methods may improve customer retention.

5. **Customers without Online Security and Tech Support show higher churn.**  
   Bundling or promoting these services may improve customer retention.

6. **Fiber optic customers show higher churn.**  
   Service quality, pricing, and customer experience should be investigated for this segment.

---

## 13. Power BI Dashboard

An interactive Power BI dashboard was developed to visualize customer churn and business insights.

The dashboard contains:

- Total Customers
- Overall Churn Rate
- Overall Churn Distribution
- Churn by Contract Type
- Churn by Payment Method
- Churn by Internet Service
- Churn Across Tenure Groups
- Churn by Monthly Charge Groups

The Power BI dashboard file is:

`customer_churn_dashboard.pbix`

---

## 14. Streamlit Prediction Application

A Streamlit application was developed to provide an interactive churn prediction interface.

Users can enter:

- Customer profile information
- Subscription details
- Internet and service information
- Billing details

The application uses the trained Logistic Regression model to predict whether a customer is likely to churn.

The application provides a clear prediction result:

- Customer is likely to churn
- Customer is unlikely to churn

The Streamlit application is located at:

`app/app.py`

---

## 15. Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- XGBoost
- Joblib
- Jupyter Notebook
- Power BI
- Streamlit
- Git/GitHub
- VS Code

---

## 16. Project Structure

```text
Customer-Churn-Prediction/
│
├── app/
│   └── app.py
│
├── data/
│   ├── raw/
│   │   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   └── cleaned_customer_churn.csv
│
├── models/
│   ├── logistic_regression_model.pkl
│   ├── preprocessor.pkl
│   ├── model_comparison.csv
│   └── selected_features.csv
│
├── notebooks/
│   └── customer_churn_analysis.ipynb
│
├── screenshots/
│   ├── model_comparison.png
│   └── streamlit_prediction.png
│
├── dashboard/
│
├── src/
│
├── customer_churn_dashboard.pbix
│
└── README.md
