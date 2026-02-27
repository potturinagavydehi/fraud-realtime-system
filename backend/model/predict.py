import joblib
import numpy as np

model = joblib.load("model/saved_model.pkl")

def predict_score(features):
    prob = model.predict_proba([features])[0][1]
    return prob