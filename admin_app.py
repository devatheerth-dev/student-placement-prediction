
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Admin Analytics",
    page_icon="📊",
    layout="wide"
)

# Load dataset
df = pd.read_csv("student_performance_placement_dataset.csv")

st.title("📊 Admin Analytics Dashboard")
st.caption("Student Performance & Placement Analytics")

st.divider()

# -----------------------------
# KPI Cards
# -----------------------------
total_students = len(df)
placed_students = (df["placement_status"] == "Placed").sum()
not_placed_students = (df["placement_status"] == "Not Placed").sum()
placement_rate = (placed_students / total_students) * 100

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Students", total_students)

with col2:
    st.metric("Placed Students", placed_students)

with col3:
    st.metric("Not Placed", not_placed_students)

with col4:
    st.metric("Placement Rate", f"{placement_rate:.2f}%")

st.divider()

# -----------------------------
# Placement Analytics
# -----------------------------
st.header("🎯 Placement Analytics")

placement_counts = df["placement_status"].value_counts()

st.bar_chart(placement_counts)

# -----------------------------
# Performance Analytics
# -----------------------------
st.header("📚 Performance Distribution")

performance_counts = df["performance_category"].value_counts()

st.bar_chart(performance_counts)

# -----------------------------
# Degree-wise Placement
# -----------------------------
st.header("🎓 Degree-wise Placement Rate")

degree_placement = (
    df.groupby("degree")["placement_status"]
    .apply(lambda x: (x == "Placed").mean() * 100)
    .sort_values(ascending=False)
)

st.bar_chart(degree_placement)

# -----------------------------
# Skill Analysis
# -----------------------------
st.header("💻 Skill Analysis")

skill_analysis = df.groupby("placement_status")[
    [
        "coding_skill",
        "communication_skill",
        "aptitude_score",
        "technical_interview_score"
    ]
].mean().round(2)

st.dataframe(
    skill_analysis,
    use_container_width=True
)

# -----------------------------
# Academic & Career Statistics
# -----------------------------
st.header("📈 Academic & Career Statistics")

stats = pd.DataFrame({
    "Metric": [
        "Average CGPA",
        "Average Attendance",
        "Average Coding Skill",
        "Average Communication Skill",
        "Average Projects",
        "Average Internships",
        "Average Resume Score"
    ],
    "Value": [
        df["cgpa"].mean(),
        df["attendance_percentage"].mean(),
        df["coding_skill"].mean(),
        df["communication_skill"].mean(),
        df["projects_completed"].mean(),
        df["internships_completed"].mean(),
        df["resume_score"].mean()
    ]
})

stats["Value"] = stats["Value"].round(2)

st.dataframe(
    stats,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.caption(
    "Admin Analytics | AI-Powered Student Performance & Placement Prediction System"
)
