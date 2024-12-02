# Heart-Risk-Prediction README

## Table of Contents
1. [Overview](#1-overview)
2. [Dataset](#2-dataset)
3. [Methodology](#3-methodology)
4. [Model Details](#4-model-details)
5. [How to Run the Project](#5-how-to-run-the-project)
   - 5.1 [Prerequisites](#51-prerequisites)
   - 5.2 [Installation](#52-installation)
   - 5.3 [Run the Streamlit App](#53-run-the-streamlit-app)
6. [API Deployment](#6-api-deployment)
7. [UI Application](#7-ui-application)
8. [Results](#8-results)
9. [Contributing](#9-contributing)
10. [License](#10-license)

## 1. Overview
**Heart Risk Prediction** is a machine learning-based tool designed to predict the likelihood of heart disease in individuals. By analyzing factors such as demographics, lifestyle choices, and medical history, the model can assist healthcare organizations in identifying high-risk patients and enabling early intervention.

## 2. Dataset
The dataset contains health-related indicators, including:
- **Demographics**: Age, gender, income, education level.
- **Medical History**: High blood pressure, cholesterol, diabetes, stroke history.
- **Lifestyle Factors**: Smoking, alcohol consumption, physical activity, diet (fruit and vegetable consumption).
- **Self-Assessments**: General health, mental health, and physical health.

### Data Preprocessing:
- Missing value imputation.
- Addressing class imbalance using Random Over-Sampling.
- Standard scaling for continuous variables.
- One-hot and ordinal encoding for categorical variables.

## 3. Methodology

### Data Collection:
The dataset is sourced from **Kaggle's Heart Disease Health Indicators**.

### Data Preprocessing:
- Handling missing data.
- Normalization and encoding.
- Feature selection based on Random Forest feature importance.

### Model Development:
- Models used: Naive Bayes, Logistic Regression, Decision Trees, Random Forest, Gradient Boosting, XGBoost, AdaBoost, and ANN.
- Hyperparameter tuning was applied only to Random Forest and XGBoost for better performance.

### Evaluation Metrics:
- Accuracy, Precision, Recall, F1 Score, ROC-AUC for model evaluation.

## 4. Model Details

- **Best Model**: Random Forest.
- **Performance Metrics**:
  - Accuracy: **94.16%**
  - ROC-AUC: **0.984**
  
- **Important Features**:
  - BMI, Age, Mental Health, Physical Activity, General Health.

## 5. How to Run the Project

### 5.1. Prerequisites
- Python 3.7 or higher.
- Virtual environment (recommended).
- Required libraries listed in `requirements.txt`.

### 5.2. Installation

- **Clone the Repository:**
```bash
git clone https://github.com/yourusername/heart-risk-prediction.git
cd heart-risk-prediction

