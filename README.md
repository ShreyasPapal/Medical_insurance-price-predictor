# 🏥 Medical Insurance Price Predictor

A Machine Learning-based web application that predicts an individual's estimated medical insurance cost based on personal and lifestyle-related factors.

The project uses **XGBoost Regression** to estimate insurance expenses and provides an interactive interface built using Streamlit.

## 📌 Project Overview

Medical insurance costs vary depending on several factors, including age, BMI, smoking habits, number of children, and geographical region.

This project aims to use Machine Learning to identify patterns in these factors and predict an estimated medical insurance cost.

Users can enter their details through a simple web interface and receive an instant prediction.

## ✨ Features

- **Insurance Cost Prediction:** Estimates medical insurance costs using an XGBoost regression model.
- **Interactive Interface:** Simple and user-friendly Streamlit application.
- **BMI Categorization:** Automatically classifies BMI into Underweight, Normal, Overweight, and Obese.
- **Multiple Input Features:** Takes age, sex, BMI, number of children, smoking status, and region as inputs.
- **Prediction History:** Maintains a session-based history of previous predictions.
- **Clear History:** Allows users to clear their prediction history.

## 🧠 Machine Learning Model

The project uses **XGBoost (Extreme Gradient Boosting) Regression**.

XGBoost is an ensemble learning algorithm that builds multiple decision trees sequentially, where each new tree attempts to correct the errors made by previous trees.

It is particularly useful for regression problems involving nonlinear relationships between input features and the target variable.

### Input Features

| Feature | Description |
|---|---|
| Age | Age of the individual |
| Sex | Male or Female |
| BMI | Body Mass Index |
| Children | Number of dependent children |
| Smoker | Smoking status (Yes/No) |
| Region | Residential region |

### Target Variable

- **Charges:** Estimated medical insurance cost.

## 🛠️ Technologies Used

- **Python** – Programming language
- **Pandas** – Data manipulation
- **NumPy** – Numerical computations
- **Scikit-learn** – Machine Learning utilities
- **XGBoost** – Regression model
- **Joblib** – Model serialization and loading
- **Streamlit** – Web application development

## 📂 Project Structure

```text
Medical_insurance-price-predictor/
│
├── data/
│   └── insurance.csv
│
├── models/
│   └── best_model.pkl
│
├── notebooks/
│   └── model_training.ipynb
│
├── app.py
├── README.md
└── requirements.txt
```

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/ShreyasPapal/Medical_insurance-price-predictor.git
```

### 2. Navigate to the Project Directory

```bash
cd Medical_insurance-price-predictor
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install streamlit pandas numpy scikit-learn xgboost joblib
```

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

## 🚀 How to Use

1. Launch the Streamlit application.
2. Enter the individual's age.
3. Select sex and geographical region.
4. Enter BMI and number of children.
5. Select smoking status.
6. Click the **Predict** button.
7. View the estimated medical insurance cost.
8. Check previous predictions in the Prediction History section.

## 🔮 Future Improvements

- Experiment with additional regression algorithms.
- Improve model performance through hyperparameter tuning.
- Add visualizations to understand the impact of different features.
- Deploy the application using Streamlit Community Cloud.
- Explore additional features to improve prediction accuracy.

## ⚠️ Disclaimer

This application is developed for educational and machine learning demonstration purposes. Predictions are estimates based on the trained model and should not be considered actual insurance quotations or professional financial advice.

## 👨‍💻 Author

**Shreyas Papal**

GitHub: [@ShreyasPapal](https://github.com/ShreyasPapal)

---

⭐ If you find this project interesting, consider giving the repository a star!
