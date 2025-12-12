from flask import Flask, request
import pandas as pd
import joblib

app = Flask(__name__)

def load_model():
    model = joblib.load(r'C:\Users\yahaf\OneDrive\Desktop\telcom-project\model\telco.joblib')
    return model

def get_data_frame(data):
    df = pd.DataFrame({
        "gender": [data.get("gender")],
        "SeniorCitizen": [data.get("SeniorCitizen")],
        "Partner": [data.get("Partner")],
        "Dependents": [data.get("Dependents")],
        "tenure": [int(data.get("tenure"))],
        "PhoneService": [data.get("PhoneService")],
        "MultipleLines": [data.get("MultipleLines")],
        "InternetService": [data.get("InternetService")],
        "OnlineSecurity": [data.get("OnlineSecurity")],
        "OnlineBackup": [data.get("OnlineBackup")],
        "DeviceProtection": [data.get("DeviceProtection")],
        "TechSupport": [data.get("TechSupport")],
        "StreamingTV": [data.get("StreamingTV")],
        "StreamingMovies": [data.get("StreamingMovies")],
        "Contract": [data.get("Contract")],
        "PaperlessBilling": [data.get("PaperlessBilling")],
        "PaymentMethod": [data.get("PaymentMethod")],
        "MonthlyCharges": [float(data.get("MonthlyCharges"))],
        "TotalCharges": [float(data.get("TotalCharges"))]
    })
    return df

@app.route('/predict', methods=['PUT'])
def predict():
    model = load_model()
    data = request.form
    input_data = get_data_frame(data)
    return str(model.predict(input_data)[0])

app.run()
#this is a comment
