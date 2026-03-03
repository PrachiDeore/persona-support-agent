import streamlit as st
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob
import json
import random
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# ==============================
# LOAD MODEL & VECTORIZER
# ==============================

model = joblib.load("persona_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# ==============================
# FASTAPI INIT
# ==============================

app = FastAPI()

# ==============================
# LOAD KNOWLEDGE BASE
# ==============================

with open("kb.json") as f:
    KB = json.load(f)

# ==============================
# MEMORY STORAGE
# ==============================

chat_memory = []

# ==============================
# REQUEST MODEL
# ==============================

class Query(BaseModel):
    message: str

# ==============================
# 1️⃣ PERSONA DETECTION (ML)
# ==============================

def detect_persona(message):
    X = vectorizer.transform([message])
    prediction = model.predict(X)[0]
    probabilities = model.predict_proba(X)[0]
    confidence = float(max(probabilities))
    return prediction, confidence

# ==============================
# 2️⃣ KNOWLEDGE RETRIEVAL
# ==============================

def retrieve_kb(persona, message):
    message = message.lower()
    persona_kb = KB.get(persona, {})

    for keyword in persona_kb:
        if keyword in message:
            return persona_kb[keyword]

    return None

# ==============================
# 3️⃣ SENTIMENT ANALYSIS
# ==============================

def analyze_sentiment(message):
    blob = TextBlob(message)
    return blob.sentiment.polarity

# ==============================
# 4️⃣ ESCALATION LOGIC
# ==============================

def should_escalate(sentiment, message):
    if sentiment < -0.6:
        return True
    if "cancel" in message.lower():
        return True
    if "complaint" in message.lower():
        return True
    return False

# ==============================
# 5️⃣ TONE ADAPTATION
# ==============================

def adapt_tone(persona, response):
    if persona == "technical":
        return f"Based on your technical query, {response}"
    elif persona == "frustrated":
        return f"I completely understand your frustration. {response}"
    elif persona == "executive":
        return f"From a business perspective, {response}"
    return response

# ==============================
# MAIN CHAT ENDPOINT
# ==============================

@app.post("/chat")
def chat(query: Query):

    user_message = query.message

    # Persona Detection
    persona, persona_confidence = detect_persona(user_message)

    # KB Retrieval
    kb_response = retrieve_kb(persona, user_message)

    # Sentiment
    sentiment = analyze_sentiment(user_message)

    # Confidence Score Calculation
    confidence = round(
        (persona_confidence * 0.7) +
        (0.2 if kb_response else 0.05) +
        random.uniform(0, 0.05),
        2
    )

    # Escalation Check
    if should_escalate(sentiment, user_message):
        response = "I understand your concern. I’m escalating this to a human specialist immediately."

        return {
            "response": response,
            "persona": persona,
            "confidence": confidence,
            "sentiment_score": sentiment,
            "escalated": True,
            "handoff_context": {
                "original_message": user_message,
                "persona": persona,
                "sentiment": sentiment,
                "chat_history": chat_memory
            }
        }

    # Generate Response
    if kb_response:
        response = adapt_tone(persona, kb_response)
    else:
        response = "Could you please provide more details?"

    # Store in Memory
    chat_memory.append({
        "user": user_message,
        "persona": persona,
        "sentiment": sentiment,
        "bot": response
    })

    return {
        "response": response,
        "persona": persona,
        "confidence": confidence,
        "sentiment_score": sentiment,
        "chat_history": chat_memory,
        "escalated": False
    }

# ==============================
# SERVE FRONTEND
# ==============================

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse("static/index.html")