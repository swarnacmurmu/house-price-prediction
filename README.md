# 🏠 House Price Prediction App

A Machine Learning web application that predicts house prices based on important house features such as area, quality, garage size, neighborhood, and construction year.

The application is built using Python, XGBoost, and Streamlit.

---

# 🚀 Features

- Predicts house prices using Machine Learning
- Uses XGBoost regression model
- Displays prediction in both INR and USD
- Interactive Streamlit dashboard
- Model comparison between:
  - Linear Regression
  - Random Forest
  - Gradient Boosting
  - XGBoost
- Feature importance visualization
- Clean and responsive UI

---

# 🧠 Machine Learning Concepts Used

## 1. Data Preprocessing
- Handling missing values
- Feature selection
- One-hot encoding

## 2. Regression Models
- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

## 3. Model Evaluation Metrics
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

## 4. Feature Importance
Used to identify which features contribute most to house price prediction.

---

# 📊 Final Model Performance

| Model | MAE | RMSE | R² Score |
|---|---|---|---|
| XGBoost | 16193.82 | 26148.24 | 0.9109 |
| Gradient Boosting | 17572.96 | 28318.73 | 0.8954 |
| Random Forest | 17596.12 | 28610.74 | 0.8933 |
| Linear Regression | 20236.41 | 51392.66 | 0.6557 |

---

# 🛠️ Tech Stack

## Frontend
- Streamlit

## Backend / ML
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Joblib

## Visualization
- Matplotlib

## Version Control
- Git
- GitHub

---

# 📂 Project Structure

```text
house-price-prediction/
│
├── app.py
├── train_model.py
├── compare_models.py
├── feature_importance.py
├── requirements.txt
├── README.md
│
├── data/
│   └── train.csv
│
├── model/
│   ├── house_price_model.pkl
│   ├── model_columns.pkl
│   ├── model_comparison.csv
│   └── feature_importance.png