import streamlit as st
import pickle
import os

# ---------- Page Config ----------
st.set_page_config(
    page_title="Fake Job Detector",
    page_icon="🕵️",
    layout="centered"
)

# ---------- Header ----------
st.title("🕵️ Fake Job Post Detector")
st.markdown(
    """
    Paste a **job description** below and let the AI predict  
    whether it is **Fake ⚠️** or **Genuine ✅**.
    """
)

st.markdown("---")

# ---------- Load Model ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "fake_job_model.pkl")
model = pickle.load(open(model_path, "rb"))

# ---------- Input ----------
text = st.text_area(
    "📄 Job Description",
    placeholder="Example: We are hiring freshers. No interview. Pay ₹30,000/week. Click the link to register...",
    height=200
)

# ---------- Prediction ----------
if st.button("🔍 Check Job Authenticity"):
    if text.strip() == "":
        st.warning("⚠️ Please enter a job description.")
    else:
        prediction = model.predict([text])[0]

        # 0 = Fake, 1 = Genuine
        if prediction == 0:
            st.error("⚠️ This looks like a **FAKE job post**.")
        else:
            st.success("✅ This looks like a **GENUINE job post**.")

st.markdown("---")
st.caption("🚀 Built by Suyash Tamkhane | AI-powered Fake Job Detection")
