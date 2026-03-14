import streamlit as st
#from zoro_chatbot import zoro_chatbot

st.set_page_config(
    page_title="FuturePath AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 FuturePath AI – Intelligent Career Advisor")

st.markdown("""
Discover your ideal career path using AI insights.
This platform helps you analyze your skills, explore careers,
build learning roadmaps, and plan your financial future.
""")

st.subheader("Skill Input")

skills = st.text_input("Enter your technical skills")
soft_skills = st.text_input("Enter your soft skills")
interests = st.text_input("Enter your interests")

experience = st.slider("Years of Experience", 0, 20, 1)

education = st.selectbox(
    "Education Level",
    ["High School", "Diploma", "Bachelor's", "Master's", "PhD"]
)

industry = st.selectbox(
    "Preferred Industry",
    ["Technology", "Finance", "Healthcare", "Design", "Marketing"]
)

if st.button("Analyze Career"):
    st.success("AI career analysis feature coming next 🚀")

st.divider()

st.subheader("Learning Roadmap")
st.write("AI will generate your learning roadmap here.")

st.subheader("Course Recommendations")
st.write("Relevant courses will appear here.")

st.subheader("Financial Planning")
st.write("Salary projections and career investment insights.")

# Floating chatbot
zoro_chatbot()
