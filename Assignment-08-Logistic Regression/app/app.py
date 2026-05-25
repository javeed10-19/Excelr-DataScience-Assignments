import streamlit as st
import pickle
import numpy as np

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Diabetes Prediction System",
    page_icon="🩺",
    layout="centered"
)

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("model\diabetes_model.pkl", "rb"))

# ---------------- CUSTOM CSS ----------------
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }

    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #0E76A8;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: gray;
        margin-bottom: 30px;
    }

    .stButton>button {
        width: 100%;
        background-color: #0E76A8;
        color: white;
        border-radius: 10px;
        height: 50px;
        font-size: 18px;
        font-weight: bold;
        border: none;
    }

    .result-box {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        margin-top: 20px;
    }

    .footer {
        text-align: center;
        color: gray;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="title">🩺 Diabetes Prediction System</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Enter patient details to predict diabetes risk</div>',
    unsafe_allow_html=True
)

# ---------------- INPUT SECTION ----------------
with st.container():

    col1, col2 = st.columns(2)

    with col1:
        preg = st.number_input("Pregnancies", 0, 20, 1)
        glucose = st.slider("Glucose Level", 0, 200, 100)
        bp = st.slider("Blood Pressure", 0, 140, 70)
        skin = st.slider("Skin Thickness", 0, 100, 20)

    with col2:
        insulin = st.slider("Insulin", 0, 900, 80)
        bmi = st.slider("BMI", 0.0, 70.0, 25.0)
        dpf = st.slider("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
        age = st.slider("Age", 1, 100, 30)

# ---------------- PREDICTION ----------------
if st.button("🔍 Predict Diabetes Risk"):

    input_data = np.array([
        [preg, glucose, bp, skin, insulin, bmi, dpf, age]
    ])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]

    st.markdown("## Prediction Result")

    if prediction[0] == 1:
        st.markdown(
            f"""
            <div class="result-box" style="background-color:#ffebee;color:#c62828;">
                ⚠️ High Risk of Diabetes<br><br>
                Probability: {probability:.2f}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div class="result-box" style="background-color:#e8f5e9;color:#2e7d32;">
                ✅ Low Risk of Diabetes<br><br>
                Probability: {probability:.2f}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.progress(int(probability * 100))

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    '<div class="footer">Built with Streamlit | Logistic Regression Model</div>',
    unsafe_allow_html=True
)