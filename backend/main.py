from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from model.predict import predict_score
from simulator import generate_transaction
from decision_engine import rule_score, final_decision

app = FastAPI(title="Real-Time Fraud Detection API")

# Transaction schema
class TransactionInput(BaseModel):
    Time: float
    amount: float
    V: List[float]
    velocity: int
    is_foreign: bool

# ----- Endpoints -----
@app.get("/simulate", tags=["Simulator"])
def simulate_transaction_endpoint():
    tx = generate_transaction()
    return tx

@app.post("/predict", tags=["ML Model"])
def predict_endpoint(transaction: TransactionInput):
    features = [transaction.Time, transaction.amount, *transaction.V]
    score = predict_score(features)
    return {"ml_score": score}

@app.post("/decision", tags=["Decision Engine"])
def decision_endpoint(transaction: TransactionInput):
    features = [transaction.Time, transaction.amount, *transaction.V]
    ml = predict_score(features)
    rule = rule_score(transaction.dict())
    final_score, decision = final_decision(ml, rule)
    return {
        "ml_score": ml,
        "rule_score": rule,
        "final_score": final_score,
        "decision": decision
    }