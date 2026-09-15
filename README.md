Customer Churn Prediction & Business Analytics using Machine Learning
Project Overview

Customer churn is an important business problem where customers discontinue a service or subscription. Predicting customer churn helps businesses identify customers who are likely to leave and take appropriate retention actions.

This project develops a complete Data Science solution for analyzing customer behavior and predicting customer churn using Machine Learning. The project includes data preprocessing, exploratory data analysis, customer behavior analysis, feature engineering, feature selection, machine learning model development, model comparison, feature importance analysis, business insights, an interactive Power BI dashboard, and a Streamlit prediction application.

Team Members
Name	Program	Domain
JAYAKUMAR	Career-Advancement	Data Science
Ashmita Thiyam	Instructor-Led	Data Science
Ishwa Patel	Instructor-Led	Data Science
PRIYANKA P	Instructor-Led	Data Science
Riddhima Gangrade	Instructor-Led	Data Science
1. Objectives

The main objectives of this project are:

Analyze customer behavior and churn patterns.
Clean and preprocess customer data.
Perform exploratory data analysis.
Identify important factors affecting customer churn.
Perform customer behavior analysis.
Perform feature engineering.
Perform feature selection.
Develop Machine Learning models for churn prediction.
Compare different Machine Learning algorithms.
Evaluate model performance.
Analyze feature importance.
Generate business insights.
Build an interactive Power BI dashboard.
Develop a Streamlit-based customer churn prediction interface.
2. Dataset

The project uses the IBM Telco Customer Churn Dataset.

Dataset Information
Total records: 7043
Features: 20 input features
Target variable: Churn
Churn classes:
Yes
No

The dataset contains information related to:

Customer demographics
Gender
Senior citizen status
Partner and dependents
Tenure
Phone services
Internet services
Online security
Online backup
Device protection
Technical support
Streaming services
Contract type
Payment method
Monthly charges
Total charges
3. Data Cleaning and Preprocessing

The following preprocessing steps were performed:

Loaded the customer churn dataset using Pandas.
Checked the dataset structure using info() and head().
Checked for missing values.
Converted the TotalCharges column from object type to numeric.
Invalid or blank values in TotalCharges were converted to missing values.
Rows containing missing TotalCharges values were removed.
The cleaned dataset contains 7032 customer records.
Categorical variables were encoded using One-Hot Encoding for Machine Learning.
Numerical variables were processed using a Column Transformer.

The cleaned dataset was saved as:

data/cleaned_customer_churn.csv

4. Exploratory Data Analysis

Exploratory Data Analysis was performed to understand customer characteristics and identify patterns related to churn.

Churn Distribution

The cleaned dataset contains:

Customers who did not churn: 5163
Customers who churned: 1869
Overall churn rate: approximately 26.58%
Customer Demographics

Gender was analyzed to understand whether churn differed significantly between male and female customers.

The analysis showed that gender has only a small difference in churn rate.

Senior Citizen Analysis

Senior citizens showed a higher churn rate compared with non-senior customers.

Non-senior customer churn: approximately 23.65%
Senior customer churn: approximately 41.68%
Customer Tenure

Customers with shorter tenure were more likely to churn.

Average tenure:

Non-churned customers: approximately 37.65 months
Churned customers: approximately 17.98 months
Contract Type

Contract type was found to be one of the strongest factors affecting churn.

Churn rates:

Month-to-month: approximately 42.71%
One year: approximately 11.28%
Two year: approximately 2.85%
Monthly Charges

Churned customers had higher average monthly charges.

Average monthly charges:

Non-churned customers: approximately $61.31
Churned customers: approximately $74.44
Payment Method

Electronic check customers showed a significantly higher churn rate.

Churn rates:

Bank transfer (automatic): approximately 16.73%
Credit card (automatic): approximately 15.25%
Electronic check: approximately 45.29%
Mailed check: approximately 19.20%
Internet Service

Fiber optic customers showed a relatively high churn rate compared with DSL and customers without internet service.

Online Security and Technical Support

Customers without Online Security and Technical Support showed higher churn rates.

This indicates that additional support and security services may be associated with better customer retention.

5. Customer Behavior Analysis

Customer behavior was analyzed using demographic, subscription, service usage, billing, and tenure-related factors.

Important observations include:

Customers with month-to-month contracts have a high churn rate.
Customers with short tenure are more likely to leave.
Customers with higher monthly charges show greater churn.
Electronic check users have a high churn rate.
Senior citizens have higher churn compared with non-senior customers.
Customers without Online Security and Technical Support have higher churn.
Fiber optic customers show relatively high churn.
Long-term contract customers have much lower churn rates.
6. Feature Engineering

Feature engineering was performed to create additional useful representations of customer information.

A tenure-based categorical feature was created:

TenureGroup

The tenure groups are:

0-12 months
13-24 months
25-36 months
37-48 months
49-60 months
61-72 months

This grouping helps analyze how churn changes across different customer lifecycle stages.

7. Feature Selection

Feature selection was performed using the SelectKBest method with the ANOVA F-test (f_classif).

The selected features included:

tenure
MonthlyCharges
TotalCharges
InternetService_Fiber optic
InternetService_No
OnlineSecurity_No internet service
OnlineBackup_No internet service
DeviceProtection_No internet service
TechSupport_No internet service
StreamingTV_No internet service
StreamingMovies_No internet service
Contract_Two year
PaperlessBilling_Yes
PaymentMethod_Electronic check
TenureGroup_61-72 months

The selected features were saved in:

models/selected_features.csv

8. Machine Learning Model Development

Multiple Machine Learning algorithms were developed and evaluated for customer churn prediction.

The models used were:

Logistic Regression
Decision Tree
Random Forest
XGBoost

The Machine Learning workflow included:

Train-test splitting
Categorical feature encoding
Feature preprocessing
Model training
Prediction
Model evaluation
Model comparison

The dataset was divided into:

Training set: 5625 records
Testing set: 1407 records
9. Model Comparison

The following models were compared based on accuracy:

Model	Accuracy
Logistic Regression	80.38%
Decision Tree	78.96%
Random Forest	75.27%
XGBoost	79.74%
Best Model

Logistic Regression achieved the highest accuracy of approximately 80.38% among the evaluated models.

Therefore, Logistic Regression was selected as the primary model for the Streamlit prediction application.

The model comparison results were saved in:

models/model_comparison.csv

10. Model Evaluation

Model performance was evaluated using classification metrics including:

Accuracy
Precision
Recall
F1-score
Classification report

For the Logistic Regression model:

Accuracy: approximately 80.38%
Churn recall: approximately 56%
Churn F1-score: approximately 60%

The evaluation helps determine how effectively the model identifies customers who are likely to churn.

11. Feature Importance Analysis

Feature importance was analyzed using the coefficients of the Logistic Regression model.

Important factors influencing churn included:

Month-to-month contract
Two-year contract
Fiber optic internet service
Electronic check payment method
Senior citizen status
Online Security
Technical Support
Customer tenure
Monthly charges
Dependents
Paperless billing
Important Observations

Positive coefficients indicate factors associated with higher churn probability, while negative coefficients indicate factors associated with lower churn probability.

Month-to-month contracts were strongly associated with increased churn, while long-term contracts were associated with lower churn.

12. Business Insights

The analysis provides several useful business insights.

1. Month-to-Month Customers Are High Risk

Customers with month-to-month contracts have a significantly higher churn rate.

Business recommendation:

Businesses can encourage customers to move to one-year or two-year contracts through discounts, loyalty benefits, or special offers.

2. New Customers Have Higher Churn

Customers with shorter tenure have a higher probability of leaving.

Business recommendation:

Companies should focus on onboarding programs, early engagement, and retention offers during the first year.

3. Electronic Check Users Show High Churn

Electronic check customers have a significantly higher churn rate.

Business recommendation:

Businesses can encourage automatic payment methods such as bank transfers or credit cards.

4. Higher Monthly Charges Are Associated With Churn

Churned customers have higher average monthly charges.

Business recommendation:

Companies can review pricing, provide personalized plans, and offer suitable discounts to high-risk customers.

5. Lack of Support Services Is Associated With Higher Churn

Customers without Online Security and Technical Support show higher churn rates.

Business recommendation:

Businesses can promote support and security services as part of customer retention strategies.

6. Senior Citizens Have Higher Churn

Senior customers show a higher churn rate.

Business recommendation:

Dedicated support, simplified service options, and personalized retention programs can be considered.

13. Power BI Interactive Dashboard

An interactive Power BI dashboard was developed to visualize customer churn patterns and business insights.

Dashboard Components

The dashboard includes:

Total Customers
Churn Rate
Overall Churn Distribution
Churn by Contract Type
Churn by Payment Method
Churn by Internet Service
Churn Across Tenure
Churn vs Monthly Charges

The Power BI dashboard file is:

customer_churn_dashboard.pbix

14. Streamlit Prediction Application

A Streamlit application was developed to provide an interactive customer churn prediction interface.

The application allows users to enter customer information such as:

Gender
Senior citizen status
Partner
Dependents
Tenure
Phone service
Internet service
Online security
Online backup
Device protection
Technical support
Streaming services
Contract type
Payment method
Paperless billing
Monthly charges
Total charges

The trained Logistic Regression model then predicts whether the customer is likely to churn.

Prediction Output

The application provides a clear prediction:

Customer is likely to churn
Customer is unlikely to churn

The Streamlit application is located at:

app/app.py

15. Technologies Used
Programming and Data Science
Python
Pandas
NumPy
Machine Learning
Scikit-learn
XGBoost
Data Visualization
Matplotlib
Seaborn
Power BI
Application Development
Streamlit
Development Environment
Jupyter Notebook
VS Code
Version Control
Git
GitHub
16. Project Structure

Customer-Churn-Prediction/

│
├── app/
│ └── app.py
│
├── data/
│ ├── raw/
│ │ └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│ │
│ └── cleaned_customer_churn.csv
│
├── models/
│ ├── logistic_regression_model.pkl
│ ├── preprocessor.pkl
│ ├── model_comparison.csv
│ └── selected_features.csv
│
├── notebooks/
│ └── customer_churn_analysis.ipynb
│
├── screenshots/
│ ├── model_comparison.png
│ ├── power_bi_dashboard.png
│ ├── streamlit.png
│ └── streamlit2.png
│
├── .gitignore
├── README.md
└── customer_churn_dashboard.pbix

17. How to Run the Project
Step 1: Clone the Repository

git clone https://github.com/IshwaPatel854/Customer-Churn-Prediction.git

Step 2: Open the Project

cd Customer-Churn-Prediction

Step 3: Create a Virtual Environment

python -m venv venv

Step 4: Activate the Virtual Environment

Windows PowerShell:

venv\Scripts\Activate.ps1

Step 5: Install Required Libraries

pip install pandas numpy matplotlib seaborn scikit-learn jupyter ipykernel streamlit joblib xgboost

Step 6: Run the Jupyter Notebook

Open:

notebooks/customer_churn_analysis.ipynb

Step 7: Run the Streamlit Application

From the project root:

streamlit run app/app.py

18. Project Deliverables

The project contains the following deliverables:

Complete source code
Raw dataset
Cleaned dataset
Jupyter Notebook
Trained Machine Learning models
Model comparison report
Feature selection results
Power BI interactive dashboard
Streamlit prediction application
Project documentation
Project screenshots
GitHub repository

19. Conclusion

The Customer Churn Prediction & Business Analytics project provides a complete Data Science solution for understanding and predicting customer churn.

The project combines data preprocessing, exploratory analysis, customer behavior analysis, feature engineering, feature selection, Machine Learning, model comparison, feature importance analysis, business insights, interactive visualization, and real-time prediction.

Among the evaluated models, Logistic Regression achieved the highest accuracy of approximately 80.38% and was selected for the Streamlit prediction application.

The analysis shows that contract type, tenure, monthly charges, payment method, internet service, and additional support services are important factors associated with customer churn.

The resulting solution can help businesses identify high-risk customers and develop targeted customer retention strategies.