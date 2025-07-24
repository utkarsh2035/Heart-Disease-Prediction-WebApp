# 💖 Heart Disease Prediction WebApp

An interactive **Streamlit** web application that predicts the risk of heart disease using patient medical data and a logistic regression model — helping users assess potential cardiac risk in seconds.

---

## 📄 Short Description

This project aims to provide a simple yet effective predictive tool for heart disease risk based on user input such as age, cholesterol, blood pressure, ECG results, and more. Built using a trained Logistic Regression model, the app transforms medical data into actionable insight.

---

## 🛠️ Tech Stack

- 🐍 **Python 3.10** – Core programming language
- 🎯 **Logistic Regression (Scikit-learn)** – For binary classification
- 🧪 **Pandas, NumPy** – For data manipulation and transformation
- 📊 **Streamlit** – For building the interactive web interface
- 🧠 **Joblib** – For model and scaler serialization
- 📦 **PKL Files** – Contains trained model, scaler, and expected feature columns

---

## 📊 Data Source

- **Source:** Open heart disease dataset  
- **Features Used:** Age, gender, chest pain type, blood pressure, cholesterol, ECG, max heart rate, exercise-induced angina, and ST segment slope

---

## 🚀 Features & Highlights

### 📌 Problem Statement

Cardiovascular diseases are among the leading causes of death worldwide. Early prediction can significantly improve treatment and outcomes. This app allows users to:

- Identify potential heart disease risk
- Understand the impact of health parameters
- Make data-driven lifestyle or medical decisions

---

## 🎯 Goal of the WebApp

To provide users with:

- ✅ A lightweight, user-friendly heart risk prediction tool
- 🩺 Real-time feedback using a trained logistic model
- 📉 Educational insight into contributing health factors

---

## 🔍 Walkthrough of Functionality

| Screenshot |
|------------|
| ![WebApp Preview](https://github.com/utkarsh2035/Heart-Disease-Prediction-WebApp/blob/main/Heart%20Desease%20Prediction.png) |

- 🔢 **Sliders & Select Boxes** — For real-time patient input
- ⚙️ **Logistic Model (86% accuracy)** — Predicts low/high heart disease risk
- 📦 **Preprocessing** — Uses scaler and one-hot encoded inputs to match model expectations
- 📋 **Model Files** — Includes `Logistic_regression_heart.pkl`, `scaler.pkl`, `columns.pkl`

---

## 📈 Key Insights

- ✅ **Logistic Regression** performed best among tested models
- 🎯 Achieved an **F1 Score of 0.88**, ensuring a good balance between precision and recall
- 🔍 Critical features influencing prediction: **age, chest pain type, cholesterol, ECG results**

---

## 📁 Project Structure

---

Heart-Disease-Prediction-WebApp/
│
├── app.py # Streamlit app code
├── Logistic_regression_heart.pkl # Trained model
├── scaler.pkl # StandardScaler for feature scaling
├── columns.pkl # Feature columns for prediction
├── requirements.txt # Required libraries
├── .gitignore # Ignored files/folders
└── README.md # Project documentation


---

## 💬 Feedback & Improvements

Planned improvements include:

- 📈 More complex models like XGBoost and ensemble voting
- 🧪 Model retraining with larger datasets for better generalization

---

## 🔖 Tags

#Streamlit #HeartDisease #MachineLearning #DataScience #Python #LogisticRegression #HealthcareAI #MLProjects
