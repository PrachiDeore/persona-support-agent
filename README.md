Persona Support Agent
Overview

Persona Support Agent is a machine learning-powered customer support chatbot that adapts its responses based on user persona.

The system detects whether the user is:

Technical

Frustrated

Executive

Based on the detected persona, it provides tone-adjusted responses using a trained ML classification model and knowledge base retrieval.

Features

ML-based Persona Detection (Scikit-learn)

TF-IDF Vectorization

Knowledge Base Response Retrieval

Sentiment Awareness

Confidence Scoring

Interactive Streamlit Interface

Cloud Deployment Ready

Project Structure

persona-support-agent/
│
├── streamlit_app.py
├── app.py (FastAPI backend version)
├── persona_model.pkl
├── vectorizer.pkl
├── kb.json
├── requirements.txt
├── runtime.txt
└── README.md

How It Works

User enters a message.

Text is transformed using TF-IDF vectorizer.

ML model predicts user persona.

System retrieves relevant response from knowledge base.

Response is displayed with detected persona and confidence score.

Installation (Local Setup)

Step 1: Clone the repository

git clone https://github.com/PrachiDeore/persona-support-agent.git

Step 2: Navigate into project folder

cd persona-support-agent

Step 3: Install dependencies

pip install -r requirements.txt

Step 4: Run the application

streamlit run streamlit_app.py

The app will open in your browser.

How To Use The App

Enter a message in the input field.

Click the Send button.

The system will:

Detect your persona

Display predicted persona

Show confidence score

Provide adaptive response

Example Inputs:

Technical:

Server authentication token failed

API returning 401 error

Frustrated:

This is the worst service ever

Nothing is working

Executive:

We need enterprise pricing details

Share budget options for our company

Deployment (Streamlit Cloud)

Push code to GitHub.

Go to https://streamlit.io/cloud

Click New App.

Select repository.

Set main file path as:

streamlit_app.py

Click Deploy.

Technologies Used

Python

Streamlit

Scikit-learn

Joblib

TF-IDF Vectorization

TextBlob (optional sentiment analysis)

Future Improvements

Add persistent chat memory

Integrate database storage

Add authentication system

Deploy Docker version

Add LLM-based response generation

Tips:
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
  
Author

Prachi Deore
Machine Learning & AI Enthusiast
