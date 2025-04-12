from flask_cors import CORS
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)
CORS(app)
# ✅ Load the trained SVM model
svm_model = joblib.load("svm_model.pkl")

@app.route('/')
def home():
    return "Welcome to the SVM Model Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    print("Received a POST request at /predict endpoint.")
    
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    print(f"File uploaded: {file.filename}")
    
    df = pd.read_excel(file)  # Read the uploaded Excel file
    print(f"Dataframe shape: {df.shape}")
    
    # Ensure input matches model requirements
    if df.shape[1] != 11680:
        return jsonify({"error": "Incorrect number of columns in dataset"}), 400

    predictions = svm_model.predict(df)
    return jsonify({"predictions": predictions.tolist()})

if __name__ == '__main__':
     app.run(host="0.0.0.0", port=8080)
