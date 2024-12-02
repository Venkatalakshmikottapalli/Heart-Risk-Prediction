import streamlit as st
import joblib

# Load the trained model
# model = joblib.load("C:/Users/venka/OneDrive/Documents/MS Documents/Yeshiva/Program documents/Fall 2024/Machine Learning/Final-Project/Heart-Risk-prediction/app/heart_disease_rf_model.pkl")

# Custom CSS 
st.markdown("""
    <style>
        body {
            background-color: white;  
            margin: 0;  
        }
        .fixed-header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #f1f1f1;  
            padding: 12px 0;
            text-align: center;
            color: black;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            z-index: 1000;
        }
        .fixed-header h1 {
            margin: 0;
            font-size: 36px;
        }
        .form-instruction {
            font-size: 20px;  
            font-weight: bold;  
            text-align: center;
            margin-top: 45px;
            margin-bottom: 20px;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f1f1f1;  
            padding: 15px;
            color: black;
            text-align: center;
            font-weight: bold;  
        }
        .stApp {
            padding-top: 140px;
            padding-bottom: 80px;  
        }
    </style>

    <div class="fixed-header">
        <br> 
        <br> 
        <h1>Check Your❤️🩺Today!</h1>
    </div>
""", unsafe_allow_html=True)

# Instruction text for the form with a custom class
st.markdown("""
<div class="form-instruction">
Please fill in all the questions and submit the form to predict your heart risk.
</div>
""", unsafe_allow_html=True)

with st.form(key="heart_health_form"):
    # User input fields
    bmi = st.text_input("1. Please enter your BMI:", "")
    age = st.text_input("2. Please enter your age:", "")
    mental_days = st.text_input("3. Number of bad mental health days last month:", "")
    physical_days = st.text_input("4. Number of bad physical health days last month:", "")

    # Dropdowns with a default empty option
    genhlth_options = ["Select an option", "Excellent", "Very Good", "Good", "Fair", "Poor"]
    genhlth = st.selectbox("5. General health level:", genhlth_options, index=0)

    education_options = ["Select an option", "No School", "Elementary School", "High School", "Some College",
                         "Associate Degree", "Bachelor's Degree", "Graduate Degree"]
    education = st.selectbox("6. Education level:", education_options, index=0)

    income_options = ["Select an option", "Less than 10k", "10k to 15k", "15k to 25k", "25k to 35k", "35k to 50k", "More than 50k"]
    income = st.selectbox("7. Income level:", income_options, index=0)

    # Radio buttons with no default selection
    gender = st.radio("8. Gender:", options=["Female", "Male"], index=None)
    highbp = st.radio("9. High Blood Pressure?", options=["No", "Yes"], index=None)
    highchol = st.radio("10. High Cholesterol?", options=["No", "Yes"], index=None)
    smoker = st.radio("11. Smoker?", options=["No", "Yes"], index=None)
    stroke = st.radio("12. Stroke history?", options=["No", "Yes"], index=None)
    prediabetes = st.radio("13. Pre-Diabetes?", options=["No", "Yes"], index=None)
    diabetes = st.radio("14. Diabetes?", options=["No", "Yes"], index=None)
    physical_activity = st.radio("15. Physical activity?", options=["No", "Yes"], index=None)
    fruit_consumption = st.radio("16. Daily fruit consumption?", options=["No", "Yes"], index=None)
    veggie_consumption = st.radio("17. Daily vegetable consumption?", options=["No", "Yes"], index=None)
    difficulty_walking = st.radio("18. Difficulty walking?", options=["No", "Yes"], index=None)

    # Submit button
    submit_button = st.form_submit_button("Predict")

# Form submission
if submit_button:
    if "" in [bmi, age, mental_days, physical_days] or \
       genhlth == "Select an option" or education == "Select an option" or income == "Select an option" or \
       None in [gender, highbp, highchol, smoker, stroke, prediabetes, diabetes, physical_activity, fruit_consumption, veggie_consumption, difficulty_walking]:
        st.error("Please fill in all fields before submitting.")
    else:
        try:
            # Convert inputs to float values
            bmi_float = float(bmi)
            age_float = float(age)
            mental_days_float = float(mental_days)
            physical_days_float = float(physical_days)

            # Map inputs
            genhlth_value = genhlth_options.index(genhlth)
            education_value = education_options.index(education)
            income_value = income_options.index(income)

            # Convert Yes/No responses to binary
            mapping = lambda x: 1 if x == "Yes" else 0
            inputs_binary = [mapping(var) for var in [highbp, highchol, smoker, stroke, prediabetes, diabetes, physical_activity, fruit_consumption, veggie_consumption, difficulty_walking]]
            sex = 1 if gender == "Male" else 0

            # Prepare input data
            input_data = [[bmi_float, mental_days_float, physical_days_float, genhlth_value, education_value,
                           income_value, age_float] + inputs_binary + [sex]]

            # Prediction
            proba = model.predict_proba(input_data)[0]
            risk_probability = proba[1]

            # Display results
            if risk_probability < 0.5:
                st.success(f"Great news! You are at a low risk for heart disease (risk probability: {risk_probability:.2f}). Keep maintaining a healthy lifestyle!")
            elif risk_probability < 0.75:
                st.warning(f"You have a moderate risk of heart disease (risk probability: {risk_probability:.2f}). Now is a great time to review your habits and make healthier choices.")
            else:
                st.error(f"High risk of heart disease detected (risk probability: {risk_probability:.2f}). It's important to consult with a healthcare provider as soon as possible to assess your health and create a plan.")
            
            # Message about key drivers
            st.info("""
            **Key Factors for Heart Disease Prediction:**
            - **Age**: Higher age groups are more susceptible.
            - **High Blood Pressure & Cholesterol**: Controllable factors, but critical risks.
            - **BMI**: Maintain a healthy weight to reduce risks.
            - **Lifestyle Choices**: Regular exercise, a balanced diet, and mental health management are essential.
            """)

        except ValueError:
            st.error("Please enter valid numerical values for BMI, Age, Mental Health, and Physical Health days.")

# Footer
st.markdown("""
    <div class="footer">
        Created with ❤️ by Venkatalakshmi Kottapalli, Yeshiva University
    </div>
""", unsafe_allow_html=True)
