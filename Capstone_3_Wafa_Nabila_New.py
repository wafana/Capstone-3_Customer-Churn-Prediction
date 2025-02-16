import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os
os.system("pip install --no-cache-dir scikit-learn")

# Load the preprocessor and model
with open("best_pipeline_new.pkl", 'rb') as f:
    best_pipeline = pickle.load(f)

# Streamlit App
st.title('E-Commerce Customer Churn Prediction')
st.text('This web can be used to predict E-commerce Customer Churn')

# Sidebar inputs
st.sidebar.header("Please input your features")

def create_user_input():
    tenure = st.sidebar.slider('Tenure', 0, 61, 12)
    warehouse_to_home = st.sidebar.slider('WarehouseToHome', 5, 127, 30)
    num_devices = st.sidebar.slider('NumberOfDeviceRegistered', 1, 6, 2)
    satisfaction_score = st.sidebar.slider('SatisfactionScore', 1, 5, 3)
    num_address = st.sidebar.slider('NumberOfAddress', 1, 21, 5)
    complain = st.sidebar.radio('Complain', [0, 1])
    days_since_last_order = st.sidebar.slider('DaySinceLastOrder', 0, 46, 10)
    cashback_amount = st.sidebar.number_input('CashbackAmount', 0.0, 324.99, 50.0)

    prefered_order_cat = st.sidebar.radio('PreferedOrderCat', ['Mobile', 'Mobile Phone', 'Grocery', 'Fashion', 'Laptop & Accessory', 'Others'])
    marital_status = st.sidebar.radio('MaritalStatus', ['Divorced', 'Married', 'Single'])

    user_data = pd.DataFrame([{
        'Tenure': tenure,
        'WarehouseToHome': warehouse_to_home,
        'NumberOfDeviceRegistered': num_devices,
        'SatisfactionScore': satisfaction_score,
        'NumberOfAddress': num_address,
        'Complain': complain,
        'DaySinceLastOrder': days_since_last_order,
        'CashbackAmount': cashback_amount,
        'PreferedOrderCat': prefered_order_cat,
        'MaritalStatus': marital_status
    }])

    return user_data

# Get user input
user_input = create_user_input()

# Predict with model
kelas = best_pipeline.predict(user_input)
probability = best_pipeline.predict_proba(user_input)[0]

# Display results
st.subheader('Prediction Result')
if kelas == 1:
    st.write('Class 1: This customer will Churn ⚠️')
else:
    st.write('Class 2: This customer will not Churn 😊')

st.write(f"Probability of Churn: {probability[1]:.2f}")  # Probability of class 1 (Churn)