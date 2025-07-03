# 🧠 Neuro Gambling Scanner - Flask API

This repository contains a Flask-based REST API for predicting gambling risk levels using a pre-trained Support Vector Machine (SVM) model. It is part of the **Neuro Gambling Scanner** project, aimed at identifying potential gambling addiction risks based on user data.

## 🚀 Features

- Accepts `.xlsx` (Excel) files with 11,680 features per record.
- Predicts risk category using a trained SVM model.
- Returns predictions in JSON format.
- Cross-Origin Resource Sharing (CORS) enabled for easy integration with front-end/mobile apps.
- Deployable via Gunicorn for production environments.

## 🗂️ Repository Structure
├── app.py # Main Flask application code
├── svm_model.pkl # Trained SVM model (11680 input features)
├── requirements.txt # Required Python packages

## 📡 API Endpoints
## ✅ GET /
Returns a welcome message.

Response:
"Welcome to the SVM Model Prediction API!"

## 🔍 POST /predict
Uploads an Excel file for prediction.

🔸 Request:
Content-Type: multipart/form-data
Field name: file
Format: .xlsx Excel file with 11680 columns

## 🧠 About the Model
Model Type: Support Vector Machine (SVM)
Input Features: 11680 (possibly EEG or behavioral signals)
Output: Risk Category → 0 (Low), 1 (Medium), 2 (High)
Trained using Scikit-learn


