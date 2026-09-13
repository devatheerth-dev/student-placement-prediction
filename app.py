
import streamlit as st
import joblib
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Student Performance & Placement Prediction",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# Load Models
# -----------------------------
placement_model = joblib.load(
    "model_artifacts/student_placement_model_v1.pkl"
)

performance_model = joblib.load(
    "model_artifacts/student_performance_model_v1.pkl"
)

# -----------------------------
# Helper Functions
# -----------------------------
def get_readiness_level(probability):

    if probability < 0.40:
        return "Low Readiness"
    elif probability < 0.70:
        return "Moderate Readiness"
    else:
        return "High Readiness"


def get_readiness_recommendation(readiness_level):

    recommendations = {
        "Low Readiness":
            "Focus on improving coding skills, communication, aptitude, "
            "projects, internships, and interview preparation.",

        "Moderate Readiness":
            "Strengthen technical skills, communication, aptitude, "
            "projects, and mock interview performance.",

        "High Readiness":
            "Maintain your current performance and continue practicing "
            "technical interviews, aptitude, and communication skills."
    }

    return recommendations[readiness_level]


def predict_student(student_data):

    student_df = pd.DataFrame([student_data])

    performance_prediction = performance_model.predict(student_df)[0]

    placement_prediction = placement_model.predict(student_df)[0]

    placement_probability = placement_model.predict_proba(
        student_df
    )[0][1]

    confidence = max(
        placement_model.predict_proba(student_df)[0]
    )

    return {
        "predicted_performance": performance_prediction,
        "placement_prediction": placement_prediction,
        "placement_probability": placement_probability,
        "placement_confidence": confidence
    }



<style>
    .main-title {
        font-size: 2.4rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.5rem;
    }

    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }

    .section-title {
        font-size: 1.4rem;
        font-weight: 600;
        margin-top: 1rem;
    }

    .result-card {
        padding: 1.2rem;
        border-radius: 12px;
        border: 1px solid #ddd;
        text-align: center;
        background: white;
    }

    .result-value {
        font-size: 1.5rem;
        font-weight: 700;
    }

    .footer {
        text-align: center;
        color: #777;
        font-size: 0.85rem;
        margin-top: 2rem;
    }
</style>


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("🎓 About the System")

    st.write(
        "An AI-powered machine learning system for predicting "
        "student academic performance and placement readiness."
    )

    st.divider()

    st.subheader("🤖 ML Models")

    st.write("• Tuned Logistic Regression")
    st.write("• Random Forest")

    st.divider()

    st.subheader("📊 Predictions")

    st.write("• Performance Category")
    st.write("• Placement Probability")
    st.write("• Placement Readiness")
    st.write("• Model Confidence")

    st.divider()

    st.warning(
        "This project uses a synthetic dataset created for "
        "demonstration and portfolio purposes."
    )

# -----------------------------
# Header
# -----------------------------
st.markdown('<div class="main-title">🎓 AI-Powered Student Performance & Placement Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Predict academic performance, placement probability, and career readiness using machine learning.</div>', unsafe_allow_html=True)

st.divider()

# -----------------------------
# Student Information
# -----------------------------
st.header("👤 Student Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=35,
        value=21
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    degree = st.selectbox(
        "Degree",
        [
            "BTech CSE",
            "BCA",
            "BBA",
            "BSc Computer Science",
            "BSc Data Science"
        ]
    )

with col2:
    year = st.selectbox(
        "Year",
        [1, 2, 3, 4]
    )

    attendance_percentage = st.number_input(
        "Attendance Percentage",
        min_value=0.0,
        max_value=100.0,
        value=80.0
    )

    study_hours_per_day = st.number_input(
        "Study Hours Per Day",
        min_value=0.0,
        max_value=15.0,
        value=3.0
    )

with col3:
    assignment_score = st.number_input(
        "Assignment Score",
        min_value=0.0,
        max_value=100.0,
        value=75.0
    )

    internal_marks = st.number_input(
        "Internal Marks",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )

    backlogs = st.number_input(
        "Backlogs",
        min_value=0,
        max_value=20,
        value=0
    )

# -----------------------------
# Skill Information
# -----------------------------
st.header("💻 Skills & Career Profile")

col1, col2, col3 = st.columns(3)

with col1:
    coding_skill = st.slider(
        "Coding Skill",
        0,
        100,
        70
    )

    communication_skill = st.slider(
        "Communication Skill",
        0,
        100,
        70
    )

    aptitude_score = st.slider(
        "Aptitude Score",
        0,
        100,
        70
    )

with col2:
    technical_interview_score = st.slider(
        "Technical Interview Score",
        0,
        100,
        70
    )

    projects_completed = st.number_input(
        "Projects Completed",
        min_value=0,
        max_value=20,
        value=2
    )

    internships_completed = st.number_input(
        "Internships Completed",
        min_value=0,
        max_value=10,
        value=1
    )

with col3:
    certifications = st.number_input(
        "Certifications",
        min_value=0,
        max_value=20,
        value=2
    )

    hackathons_participated = st.number_input(
        "Hackathons Participated",
        min_value=0,
        max_value=20,
        value=1
    )

    extracurricular_activities = st.number_input(
        "Extracurricular Activities",
        min_value=0,
        max_value=20,
        value=2
    )

# -----------------------------
# Professional Profile
# -----------------------------
st.header("📄 Professional Profile")

col1, col2, col3 = st.columns(3)

with col1:
    resume_score = st.slider(
        "Resume Score",
        0,
        100,
        70
    )

with col2:
    mock_interviews = st.number_input(
        "Mock Interviews",
        min_value=0,
        max_value=20,
        value=2
    )

with col3:
    linkedin_profile = st.selectbox(
        "LinkedIn Profile",
        ["Yes", "No"]
    )

    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        value=7.5,
        step=0.1
    )


# -----------------------------
# Prediction History
# -----------------------------
if "prediction_history" not in st.session_state:
    st.session_state.prediction_history = []

# -----------------------------
# Prediction Button
# -----------------------------
st.divider()

if st.button(
    "🚀 Predict Student Outcome",
    use_container_width=True
):

    student_data = {
        "age": age,
        "gender": gender,
        "degree": degree,
        "year": year,
        "attendance_percentage": attendance_percentage,
        "study_hours_per_day": study_hours_per_day,
        "assignment_score": assignment_score,
        "internal_marks": internal_marks,
        "backlogs": backlogs,
        "coding_skill": coding_skill,
        "communication_skill": communication_skill,
        "aptitude_score": aptitude_score,
        "technical_interview_score": technical_interview_score,
        "projects_completed": projects_completed,
        "internships_completed": internships_completed,
        "certifications": certifications,
        "hackathons_participated": hackathons_participated,
        "extracurricular_activities": extracurricular_activities,
        "resume_score": resume_score,
        "mock_interviews": mock_interviews,
        "linkedin_profile": linkedin_profile,
        "cgpa": cgpa
    }

    result = predict_student(student_data)

    probability = result["placement_probability"]

    st.session_state.prediction_history.append({
        "Performance": result["predicted_performance"],
        "Placement": result["placement_prediction"],
        "Placement Probability": f"{probability * 100:.2f}%",
        "Readiness": get_readiness_level(probability)
    })

    readiness = get_readiness_level(probability)

    recommendation = get_readiness_recommendation(
        readiness
    )

    # -----------------------------
    # Results
    # -----------------------------
    st.header("📊 Prediction Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Performance Prediction",
            result["predicted_performance"]
        )

    with col2:
        st.metric(
            "Placement Probability",
            f"{probability * 100:.2f}%"
        )

    with col3:
        st.metric(
            "Readiness Level",
            readiness
        )

    st.progress(probability)

    st.subheader("🎯 Placement Prediction")

    if result["placement_prediction"] == "Placed":
        st.success("Student is predicted to be PLACED.")
    else:
        st.warning("Student is predicted to be NOT PLACED.")

    st.subheader("💡 Recommendation")

    st.info(recommendation)

    st.subheader("🔍 Prediction Confidence")

    st.write(
        f"Model confidence: "
        f"{result['placement_confidence'] * 100:.2f}%"
    )


# -----------------------------
# Prediction History
# -----------------------------
if st.session_state.prediction_history:
    st.divider()
    st.header("📋 Prediction History")

    history_df = pd.DataFrame(
        st.session_state.prediction_history
    )

    st.dataframe(
        history_df,
        use_container_width=True,
        hide_index=True
    )


# -----------------------------
# Model Performance
# -----------------------------
st.divider()
st.header("🤖 Model Performance")

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.metric("Accuracy", "71.80%")

with metric_col2:
    st.metric("Precision", "44.70%")

with metric_col3:
    st.metric("Recall", "73.75%")

with metric_col4:
    st.metric("ROC-AUC", "79.63%")

st.caption(
    "Metrics shown are from the final placement prediction model "
    "evaluated on the held-out test set."
)

# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
    "AI-Powered Student Performance & Placement Prediction System | "
    "Machine Learning Portfolio Project"
)
