import streamlit as st
import pickle

st.set_page_config(page_title="Fake Job Detector", layout="centered")

st.title("🕵️ Fake Job Post Detector")
st.write("Paste a job description below to check if it is **Fake or Genuine**.")

# Load trained model
model = pickle.load(open("fake_job_model.pkl", "rb"))

text = st.text_area("Job Description")

if st.button("Check Job"):
    if text.strip() == "":
        st.warning("Please enter job description")
    else:
        # ✅ Use predict() ONLY (no predict_proba)
        prediction = model.predict([text])[0]

# ⚠️ Label correction
# Model predicts 1 = Genuine, 0 = Fake

if prediction == 0:
    st.error("⚠️ Fake Job Post")
else:
    st.success("✅ Genuine Job Post")
