import { useEffect, useState } from "react";

function Dashboard() {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    const fetchTransaction = async () => {
      try {
        // Simulate transaction
        const simRes = await fetch("http://127.0.0.1:8000/simulate");
        const tx = await simRes.json();

        // Get final decision
        const decisionRes = await fetch("http://127.0.0.1:8000/decision", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(tx),
        });
        const result = await decisionRes.json();

        // Keep last 20 transactions
        setTransactions(prev => [result, ...prev.slice(0, 19)]);
      } catch (err) {
        console.error(err);
      }
    };

    const interval = setInterval(fetchTransaction, 1000); // every 1s
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>Real-Time Fraud Risk Dashboard</h1>

      <table border="1" cellPadding="5">
        <thead>
          <tr>
            <th>ID</th>
            <th>Amount</th>
            <th>ML Score</th>
            <th>Rule Score</th>
            <th>Final Score</th>
            <th>Decision</th>
          </tr>
        </thead>
        <tbody>
          {transactions.map((tx, index) => (
            <tr key={index}>
              <td>{tx.id ? tx.id.slice(0, 8) : "sim"}</td>
              <td>{tx.amount?.toFixed(2)}</td>
              <td>{tx.ml_score?.toFixed(2)}</td>
              <td>{tx.rule_score?.toFixed(2)}</td>
              <td>{tx.final_score?.toFixed(2)}</td>
              <td style={{ color: tx.decision === "BLOCK" ? "red" : "green" }}>
                {tx.decision}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Dashboard;