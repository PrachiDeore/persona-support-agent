import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Small training dataset (you can expand this later)
texts = [
    "API endpoint error 500",
    "Server configuration issue",
    "Authentication token expired",
    "This is worst service",
    "I am very frustrated",
    "Nothing is working",
    "We need pricing details",
    "Budget planning discussion",
    "Enterprise solution for company"
]

labels = [
    "technical",
    "technical",
    "technical",
    "frustrated",
    "frustrated",
    "frustrated",
    "executive",
    "executive",
    "executive"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

joblib.dump(model, "persona_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained and saved!")