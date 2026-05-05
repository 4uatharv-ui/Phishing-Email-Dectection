import joblib

model = joblib.load("models/phishing_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_email(email_text):
    email_vector = vectorizer.transform([email_text])
    prediction = model.predict(email_vector)

    if prediction[0] == 1:
        return "Phishing"
    return "Safe"
