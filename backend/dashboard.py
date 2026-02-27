import streamlit as st
import requests
import time

st.set_page_config(page_title="Real-Time Fraud Dashboard", layout="wide")
st.title("Real-Time Fraud Risk Dashboard")

# Table columns
columns = ["ID", "Amount", "ML Score", "Rule Score", "Final Score", "Decision"]

transactions = []

while True:
    try:
        # Get simulated transaction
        tx = requests.get("http://127.0.0.1:8000/simulate").json()
        
        # Get final decision from backend
        decision = requests.post("http://127.0.0.1:8000/decision", json=tx).json()

        # Add ID for display
        decision["id"] = tx.get("id", f"sim{len(transactions)+1}")

        # Keep only last 20 transactions
        transactions.insert(0, decision)
        if len(transactions) > 20:
            transactions.pop()

        # Prepare table for Streamlit
        table_data = []
        for tx in transactions:
            table_data.append({
                "ID": tx["id"],
                "Amount": round(tx.get("amount",0),2),
                "ML Score": round(tx.get("ml_score",0),2),
                "Rule Score": round(tx.get("rule_score",0),2),
                "Final Score": round(tx.get("final_score",0),2),
                "Decision": tx.get("decision","")
            })

        st.table(table_data)

        time.sleep(1)  # update every 1 second
        st.empty()  # clear old table for next update

    except Exception as e:
        st.error(f"Error: {e}")
        break