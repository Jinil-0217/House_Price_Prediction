import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model.pkl')

st.title("🏠 House Price Predictor")

st.write("Upload the csv file with the house data to get predictions.")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    
    st.subheader("Uploaded Data")
    st.write(data.head())

    predictions = model.predict(data)

    data['Predicted Price'] = predictions

    st.subheader("Predictions")
    st.write(data.head())

    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button(
        "Download Predictions",
        data=csv,
        file_name='predictions.csv',    
        mime='text/csv',
    )