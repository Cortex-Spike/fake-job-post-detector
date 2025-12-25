import streamlit as st
import pickle
import os

st.set_page_config(page_title="Fake Job Detector", layout="centered")

st.title("🕵️ Fake Job Post Detector")
st.write("Paste a job description below to check if it is **Fake or Genuine**.")

# Load trained model safely
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "fake_job_model.pkl")

model = pickle.load(open(model_path, "rb"))

text = st.text_area("Job Description")

if st.button("Check Job"):
    if text.strip() == "":
        st.warning("Please enter job description")
    else:
        prediction = model.predict([text])[0]

        # 0 = Fake, 1 = Genuine
        if prediction == 0:
            st.error("⚠️ Fake Job Post")
        else:
            st.success("✅ Genuine Job Post")

st.markdown("---")
st.caption("🚀 Built by Suyash Tamkhane | Fake Job Detector")
