# House Price Prediction App

This project predicts house prices using a machine learning model built with XGBoost.

## Features
- End-to-end ML pipeline (preprocessing + model)
- Handles missing values and categorical encoding
- Achieves R² score of ~0.90
- Streamlit web app for predictions
- CSV upload + downloadable results

## Key Insights
- Overall quality is the most important factor
- Living area and garage capacity significantly impact price
- Interior quality (kitchen, basement) influences valuation

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run the app:
streamlit run app.py

## Usage
- Upload sample_input.csv
- View predictions
- Download results

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Streamlit

## Notebook
Full analysis and model building available in:
house_price_prediction.ipynb

## Workflow
1. Data Cleaning  
2. Feature Engineering  
3. Model Training (Ridge, Lasso, XGBoost)  
4. Hyperparameter Tuning  
5. Deployment using Streamlit