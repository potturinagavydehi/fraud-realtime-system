import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("../../data/creditcard.csv")

X = df.drop("Class", axis=1)
y = df["Class"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y
)

model = RandomForestClassifier(n_estimators=150, max_depth=12)
model.fit(X_train, y_train)

joblib.dump(model, "saved_model.pkl")

print("Model trained and saved.")