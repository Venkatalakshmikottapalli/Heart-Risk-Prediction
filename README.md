# Heart-Risk-Prediction
## Project Overview
The **Heart Risk Prediction** project aims to predict an individual's risk of developing heart disease using machine learning models. By leveraging patient data such as lifestyle, medical history, and demographics, the model provides valuable insights that can aid healthcare organizations in early detection and intervention.

## Table of Contents
- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Model Details](#model-details)
- [How to Run the Project](#how-to-run-the-project)
- [API Deployment](#api-deployment)
- [UI Application](#ui-application)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

---

## Directory Structure
```plaintext
HEART-RISK-PREDICTION/
├── api/
│   ├── api.py
│   └── heart_disease_rf_model.pkl
│
├── app/
│   └── main.py
│
├── data/
│   ├── processed/
│   └── raw/
│
├── doc/
│   ├── ML_Final_project_report.docx
│   └── V_Kottapalli_ML_Finalproject_ppt.pptx
│
├── model/
│   ├── .ipynb_checkpoints/
│   └── model.py
│
├── notebooks/
│   ├── V_Kottapalli_Final_Project_Modelbuilding.ipynb
│   └── V_Kottapalli_Final_Project_Preprocessing.ipynb
│
├── ui/
│   └── main.py
│
├── LICENSE
└── README.md

## Dataset
The dataset consists of patient health indicators such as:

- **Demographic Information:** Age, gender, income, education level
- **Medical History:** High blood pressure, cholesterol levels, diabetes, stroke history
- **Lifestyle Indicators:** Smoking, alcohol consumption, physical activity, diet (fruit and vegetable intake)
- **Self-Assessments:** General, mental, and physical health conditions

### Data Preprocessing Steps:
- Handling missing values
- Addressing class imbalance using Random Over-Sampling
- Standardization and encoding of categorical variables

---

## Methodology

### Data Collection:
Gathered from Kaggle's Heart Disease Health Indicators dataset.

### Data Preprocessing:
- Missing values treatment.
- Standard scaling of continuous variables.
- One-hot and ordinal encoding of categorical variables.

### Feature Engineering:
- Feature importance selection using Random Forest.
- Removal of less important features (e.g., `NoDocbcCost`, `HvyAlcoholConsump`).

### Model Training:
- Models used: Naive Bayes, Logistic Regression, Decision Trees, Random Forest, Gradient Boosting, XGBoost, AdaBoost, and ANN.
- Hyperparameter tuning for Random Forest and XGBoost.

### Evaluation Metrics:
- Accuracy, Precision, Recall, F1 Score, ROC-AUC.

---

## Model Details

- **Best Model:** Random Forest
- **Performance Metrics:**
  - Accuracy: **94.16%**
  - ROC-AUC: **0.984**

- **Feature Importance:**
  - Key features: BMI, Age, Mental Health, Physical Activity, and General Health.

---

## How to Run the Project

### Clone the Repository:
```bash
git clone https://github.com/yourusername/heart-risk-prediction.git
cd heart-risk-prediction

## UI Application

The UI is built using **Streamlit** and offers a simple interface for users to:

- Input patient health data.
- Obtain real-time heart disease risk predictions.

### Steps to Run the UI:
- Navigate to the `ui` folder.
- Run `main.py` using Streamlit.

---

## Results

- **Best Model:** Random Forest
- **Model Accuracy:** 94.16%
- **Key Insights:**
  - High BMI, poor general health, and lack of physical activity are major contributors to heart disease.
  - The model's high ROC-AUC score (0.984) indicates strong predictive performance.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Submit a pull request.

Feel free to open an issue for any feature requests or bugs.

---

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

Thank you for using **Heart Risk Prediction**!
