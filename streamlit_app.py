import streamlit as st
import joblib
import os
import numpy as np

st.set_page_config(page_title="Persona Support Agent", layout="centered")

st.title("🤖 Persona Support Agent")
st.markdown("ML-Powered Adaptive Customer Support System")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "persona_model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))

def detect_persona(message):
    X = vectorizer.transform([message])
    prediction = model.predict(X)[0]
    probabilities = model.predict_proba(X)[0]
    confidence = float(np.max(probabilities))
    return prediction, confidence

st.sidebar.header("📌 About")
st.sidebar.write("This chatbot detects user persona and adapts responses accordingly.")
st.sidebar.write("Personas: Technical | Frustrated | Executive")

st.subheader("Ask your question below 👇")

user_input = st.text_area("Enter your message")

if st.button("Send Message"):

    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        persona, confidence = detect_persona(user_input)

        st.markdown("### 🔍 Detected Persona")
        st.success(persona.capitalize())

        st.markdown("### 📊 Confidence Score")
        st.progress(int(confidence * 100))
        st.write(f"{round(confidence*100,2)}%")

        if persona == "technical":
            response = "It appears to be a technical issue. Please verify your configuration and logs."
        elif persona == "frustrated":
            response = "I understand your frustration. Let me help resolve this immediately."
        elif persona == "executive":
            response = "From a business perspective, I recommend reviewing enterprise pricing options."
        else:
            response = "Could you please provide more details?"

        st.markdown("### 💬 Response")
        st.info(response)

st.markdown("---")
st.markdown("### 💡 Example Questions You Can Try")

st.write("""
Technical:
- Server authentication token failed
- API returning 401 error
- Cloud deployment configuration issue

Frustrated:
- This is the worst service ever
- Nothing is working properly
- I want to cancel my subscription

Executive:
- We need enterprise pricing details
- Share budget options for 200 employees
- Provide corporate subscription plan
""")