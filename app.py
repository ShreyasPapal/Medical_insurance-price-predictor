import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/best_model.pkl")

st.set_page_config(
    page_title="Medical Insurance Cost Predictor",
    layout="centered"
)

with st.sidebar:
    st.header("About")

    st.write(
        "This application uses machine learning "
        "to estimate individual medical costs."
    )

    st.divider()

    st.subheader("Model")

    st.write("XGBoost")

    st.subheader("Features")

    st.write(
        "Age, sex, BMI, children, smoker and region."
    )

    st.divider()

    st.caption("Medical Cost Prediction Project")
    
if "history" not in st.session_state:
    st.session_state.history = []

st.title("Medical Insurance Cost Predictor")
st.caption("Estimate individual medical insurance costs using machine learning.")

st.divider()

st.subheader("Patient Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30,
        step=1
    )

    sex = st.selectbox(
        "Sex",
        ["male", "female"]
    )

    region = st.selectbox(
        "Region",
        ["northeast", "northwest", "southeast", "southwest"]
    )

with col2:
    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=25.0,
        step=0.1
    )

    children = st.number_input(
        "Number of Children",
        min_value=0,
        max_value=10,
        value=0,
        step=1
    )

    smoker = st.selectbox(
        "Smoker",
        ["yes", "no"]
    )

if bmi < 18.5:
    bmi_category = "Underweight"
elif bmi < 25:
    bmi_category = "Normal"
elif bmi < 30:
    bmi_category = "Overweight"
else:
    bmi_category = "Obese"

st.write(f"BMI Category: {bmi_category}")

st.divider()

if st.button("Predict", use_container_width=True):

    input_data = pd.DataFrame({
        "age": [age],
        "bmi": [bmi],
        "children": [children],
        "sex_male": [sex == "male"],
        "smoker_yes": [smoker == "yes"],
        "region_northwest": [region == "northwest"],
        "region_southeast": [region == "southeast"],
        "region_southwest": [region == "southwest"]
    })

    prediction = model.predict(input_data)[0]

    st.subheader("Estimated Medical Insurance Cost")

    st.metric(
        label="Predicted Cost",
        value=f"${prediction:,.2f}"
    )

    st.session_state.history.append({
        "Age": age,
        "Sex": sex,
        "BMI": bmi,
        "Children": children,
        "Smoker": smoker,
        "Region": region,
        "Predicted Cost": f"${prediction:,.2f}"
    })

if st.session_state.history:

    st.divider()

    st.subheader("Prediction History")

    history_df = pd.DataFrame(
        st.session_state.history
    )

    st.dataframe(
        history_df,
        use_container_width=True,
        hide_index=True
    )

    if st.button("Clear History"):
        st.session_state.history = []
        st.rerun()