import streamlit as st
import joblib
import os

st.title("Persona Support Agent")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "persona_model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))

def detect_persona(message):
    X = vectorizer.transform([message])
    prediction = model.predict(X)[0]
    return prediction

user_input = st.text_input("Enter your message")

if st.button("Send"):
    persona = detect_persona(user_input)
    st.write("Detected Persona:", persona)