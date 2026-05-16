import streamlit as st
import pickle
import numpy as np
import pandas as pd
from PIL import Image



# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
page_title="Diabetes Prediction AI",
    page_icon="🩺",
    layout="wide"
)

# ─────────────────────────────────────────────
# LOAD MODEL
# ─────────────────────────────────────────────
@st.cache_resource
def load_model():

    model = pickle.load(open('diabetes_model.save', 'rb'))

    return model

model = load_model()

# ─────────────────────────────────────────────
# CSS STYLING
# ─────────────────────────────────────────────
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Background */
.stApp {
    background: linear-gradient(135deg,#0f172a,#111827,#1e293b);
    color: white;
}

/* Main Container */
.main .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1300px;
}

/* Title */
.main-title {
    font-size: 3.3rem;
    font-weight: 700;
    color: #38bdf8;
    margin-bottom: 10px;
}
/* Subtitle */
.subtitle {
    color: #cbd5e1;
    font-size: 1rem;
    line-height: 1.8;
}

/* Glass Card */
.glass {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 22px;
    padding: 25px;
    backdrop-filter: blur(12px);
    margin-bottom: 20px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.25);
}

/* Section Title */
.section-title {
    color: #38bdf8;
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 15px;
}

/* Metric Card */
.metric-card {
    background: linear-gradient(135deg,#0ea5e9,#0284c7);
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    color: white;
    box-shadow: 0 4px 20px rgba(14,165,233,0.3);
}

.metric-number {
    font-size: 2rem;
    font-weight: 700;
}

.metric-label {
    font-size: 0.9rem;
    opacity: 0.9;
}

/* Inputs */
.stNumberInput input {
    background-color: rgba(255,255,255,0.08) !important;
    color: white !important;
    border-radius: 10px !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
}

/* Button */
.stButton button {
    width: 100%;
    background: linear-gradient(90deg,#06b6d4,#3b82f6);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 14px;
    font-size: 18px;
    font-weight: 600;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.02);
    box-shadow: 0 0 20px rgba(56,189,248,0.5);
}

/* Result Box */
.result-box {
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    font-size: 1.3rem;
    font-weight: 600;
    margin-top: 20px;
}

.success-box {
    background: rgba(16,185,129,0.15);
    border: 1px solid #10b981;
}

.danger-box {
    background: rgba(239,68,68,0.15);
    border: 1px solid #ef4444;
}

}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HEADER SECTION
# ─────────────────────────────────────────────
left_header, right_header = st.columns([1.3, 1])

with left_header:
    st.markdown("""
    <div class="main-title">
        命 Diabetes Prediction AI
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="subtitle">
        Advanced Machine Learning based Diabetes Risk Prediction System.
        Predict diabetes risk instantly using patient health information
        and Artificial Intelligence.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="glass">
        <div class="section-title">💡 About Diabetes</div>
        Diabetes is a chronic disease that occurs when blood sugar levels
        become too high. Early prediction and treatment help reduce serious
        health complications.
        <br><br>
        This AI-powered system predicts diabetes risk using medical data.
    </div>
    """, unsafe_allow_html=True)

with right_header:
    try:
        # Use the actual filename you uploaded
        image = Image.open("image_93189e.jpg")
        st.image(image, use_container_width=True)
    except Exception:
        # This removes the warning and shows a clean message if the file is missing
        st.info("ℹ️ Patient Health Visualization")
        # ─────────────────────────────────────────────
# RIGHT HEADER IMAGE
# ─────────────────────────────────────────────
with right_header:

    try:
        # use your correct image filename here
        image = Image.open("diabetes_img.jpg")

        st.image(
            image,
            use_container_width=True
        )

    except FileNotFoundError:

        st.error("Image file not found")

# ─────────────────────────────────────────────
# METRIC CARDS
# ─────────────────────────────────────────────
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">768</div>
        <div class="metric-label">Patients</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">8</div>
        <div class="metric-label">Features</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">1</div>
        <div class="metric-label">ML Model</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">AI</div>
        <div class="metric-label">Prediction</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# MAIN SECTION
# ─────────────────────────────────────────────
left, right = st.columns([1.2, 1])

# ─────────────────────────────────────────────
# LEFT SIDE INPUTS
# ─────────────────────────────────────────────
with left:

    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title">
        📋 Patient Information
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        pregnancies = st.number_input("Pregnancies", 0, 20, 1)
        glucose = st.number_input("Glucose Level", 0, 300, 120)
        blood_pressure = st.number_input("Blood Pressure", 0, 200, 70)
        skin_thickness = st.number_input("Skin Thickness", 0, 100, 20)

    with c2:
        insulin = st.number_input("Insulin", 0, 900, 80)
        bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
        dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
        age = st.number_input("Age", 1, 120, 30)

    st.markdown("</div>", unsafe_allow_html=True)

    predict_btn = st.button("🔍 Predict Diabetes")

# ─────────────────────────────────────────────
# RIGHT SIDE
# ─────────────────────────────────────────────
with right:

    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title">
        💡 Health Tips
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ✅ Exercise regularly  
    ✅ Drink more water  
    ✅ Avoid excess sugar  
    ✅ Eat healthy foods  
    ✅ Sleep properly  
    ✅ Check glucose levels  
    """)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title">
        📊 System Information
    </div>
    """, unsafe_allow_html=True)

    info_df = pd.DataFrame({
        "Feature": [
            "Pregnancies",
            "Glucose",
            "Blood Pressure",
            "Skin Thickness",
            "Insulin",
            "BMI",
            "DPF",
            "Age"
        ]
    })

    st.dataframe(info_df, use_container_width=True, hide_index=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# PREDICTION SECTION
# ─────────────────────────────────────────────
if predict_btn:

    features = np.array([[
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        dpf,
        age
    ]])

    prediction = model.predict(features)

    probability = model.predict_proba(features)[0][1]

    risk = round(probability * 100, 2)

    st.markdown("<br>", unsafe_allow_html=True)

    if prediction[0] == 1:

        st.markdown(f"""
        <div class="result-box danger-box">
            ⚠️ High Diabetes Risk Detected <br><br>

            Risk Score : {risk}% <br>

            Prediction : Positive
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div class="result-box success-box">
            ✅ Low Diabetes Risk <br><br>

            Risk Score : {risk}% <br>

            Prediction : Negative
        </div>
        """, unsafe_allow_html=True)

    st.progress(int(risk))

    # RESULT TABLE
    result_df = pd.DataFrame({
        "Feature": [
            "Pregnancies",
            "Glucose",
            "Blood Pressure",
            "Skin Thickness",
            "Insulin",
            "BMI",
            "DPF",
            "Age"
        ],
        "Value": [
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            dpf,
            age
        ]
    })

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title">
        📄 Prediction Summary
    </div>
    """, unsafe_allow_html=True)

    st.dataframe(result_df, use_container_width=True, hide_index=True)

    csv = result_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download Report",
        csv,
        "diabetes_report.csv",
        "text/csv"
    )

    st.markdown("</div>", unsafe_allow_html=True)