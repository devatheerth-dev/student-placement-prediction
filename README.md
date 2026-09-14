## 🚀 Live Demo

[👉 Open the Student Placement Prediction App](https://student-placement-prediction-xwvizappzv37gd8ebdr6vru.streamlit.app)

# AI-Powered Student Performance & Placement Prediction System

## Project Overview

An end-to-end machine learning system designed to predict student academic performance and placement outcomes using academic, technical, communication, and career-related features.

The project includes machine learning pipelines, model evaluation, explainable AI, interactive Streamlit dashboards, student prediction reports, PDF generation, and administrative analytics.

**Important:** The dataset used in this project is synthetic and does not represent real institutional student data.

## Key Features

- Student performance prediction
- Placement probability prediction
- Multiple machine learning models
- Hyperparameter tuning
- Cross-validation
- Model evaluation
- Feature importance analysis
- SHAP explainable AI
- Student readiness analysis
- Personalized recommendations
- PDF student reports
- Admin analytics dashboard
- Prediction history
- Input validation and error handling
- Versioned model artifacts

## Machine Learning

### Placement Prediction

- Final model: Tuned Logistic Regression
- Class-weight balancing
- 5-fold stratified cross-validation
- ROC-AUC based model evaluation

### Performance Prediction

- Model: Random Forest Classifier
- Class-weight balancing

## Placement Model Performance

Held-out test set results:

- Accuracy: 71.80%
- Precision: 44.70%
- Recall: 73.75%
- ROC-AUC: 79.63%

These results are specific to the synthetic dataset and should not be interpreted as real-world institutional performance.

## Explainable AI

SHAP (SHapley Additive exPlanations) is used to understand how individual features influence placement predictions.

Feature importance analysis is also included.

## Applications

### Student Dashboard

- Student input form
- Performance prediction
- Placement prediction
- Placement probability
- Readiness analysis
- Personalized recommendation
- Prediction history

### Admin Dashboard

- Overall placement statistics
- Placement distribution
- Performance distribution
- Degree-wise placement analysis
- Skill-wise analysis
- Academic and career statistics

## Project Structure

```text
student_placement_prediction/
├── app.py
├── admin_app.py
├── student_performance_placement_dataset.csv
├── requirements.txt
├── .gitignore
└── model_artifacts/
    ├── student_placement_model_v1.pkl
    ├── student_performance_model_v1.pkl
    └── model_metadata_v1.json
```

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- SHAP
- Matplotlib
- Seaborn
- Joblib
- Streamlit
- ReportLab

## Machine Learning Workflow

Data Validation → EDA → Preprocessing → Feature Engineering → Model Training → Model Comparison → Hyperparameter Tuning → Cross-Validation → Explainable AI → Final Model → Prediction System → Streamlit → Testing

## Data & Ethical Considerations

This project uses synthetic data for educational and portfolio purposes.

The system should not be used as the sole basis for real student placement decisions. Predictions contain uncertainty and should be treated as decision-support information.

## Author

Devatheerth M

BCA Data Science

Presidency University
