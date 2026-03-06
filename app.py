import streamlit as st
import PyPDF2
import matplotlib.pyplot as plt


# Load CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

skills = ["python","java","c","html","css","javascript","react","node","sql","machine learning"]

def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text=""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

def detect_skills(text):
    detected=[]
    for skill in skills:
        if skill in text:
            detected.append(skill)
    return detected

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file is not None:

    text = extract_text(uploaded_file)

    detected_skills = detect_skills(text)

    st.markdown("<div class='detected'><h3>Detected Skills</h3></div>", unsafe_allow_html=True)
    st.write(detected_skills)

    score = len(detected_skills)*10

    st.markdown("<div class='score'><h3>ATS Score</h3></div>", unsafe_allow_html=True)
    st.write(score)

    st.progress(score)

    missing = list(set(skills) - set(detected_skills))

    st.markdown("<div class='missing'><h3>Missing Skills</h3></div>", unsafe_allow_html=True)
    st.write(missing)

    # Chart
    labels = ["Detected Skills","Missing Skills"]
    values = [len(detected_skills), len(missing)]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct="%1.1f%%")
    st.pyplot(fig)

    st.subheader("Suggestions")
    st.write("Add more technical skills like React, SQL, Machine Learning to improve ATS score.")
