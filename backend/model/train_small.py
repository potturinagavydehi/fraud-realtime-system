import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load small dataset
df = pd.read_csv("../../data/creditcard_small.csv")

X = df.drop("Class", axis=1)
y = df["Class"]

# Train a lightweight Random Forest
model = RandomForestClassifier(n_estimators=50, max_depth=5, random_state=42)
model.fit(X, y)

# Save the trained model
joblib.dump(model, "saved_model_small.pkl")

print("Small ML model trained and saved!")