import { useState } from "react";
import "./App.css";

function App() {
  const [formData, setFormData] = useState({
    patient_age: "",
    claim_amount: "",
    eligibility: "",
    prior_authorization: "",
    documentation: "",
    claim_complexity: "",
    historical_denial_rate: "",
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (event) => {
    const { name, value } = event.target;

    setFormData((previous) => ({
      ...previous,
      [name]: value,
    }));
  };

  const handlePredict = async (event) => {
    event.preventDefault();

    setLoading(true);
    setResult(null);
    setError("");

    const requestData = {
      patient_age: Number(formData.patient_age),
      claim_amount: Number(formData.claim_amount),
      eligibility: Number(formData.eligibility),
      prior_authorization: Number(formData.prior_authorization),
      documentation: Number(formData.documentation),
      claim_complexity: Number(formData.claim_complexity),
      historical_denial_rate: Number(formData.historical_denial_rate),
    };

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/predict",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(requestData),
        }
      );

      if (!response.ok) {
        const errorData = await response.text();
        throw new Error(errorData);
      }

      const data = await response.json();

      setResult(data);
    } catch (error) {
      console.error("Prediction error:", error);

      setError(
        "Prediction failed. Browser Console mein error check karo."
      );
    } finally {
      setLoading(false);
    }
  };

  const handleNewPrediction = () => {
    setResult(null);
    setError("");

    setFormData({
      patient_age: "",
      claim_amount: "",
      eligibility: "",
      prior_authorization: "",
      documentation: "",
      claim_complexity: "",
      historical_denial_rate: "",
    });
  };

  return (
    <div className="app">

      {/* HEADER */}

      <header>
        <h1>Medical Claim AI</h1>

        <p>
          AI-Based Medical Claim Approval and Denial Prediction System
        </p>
      </header>


      {/* CLAIM FORM */}

      {!result && (
        <main className="card">

          <h2>Claim Prediction</h2>

          <p className="subtitle">
            Enter the claim details to predict approval or denial risk.
          </p>

          <form onSubmit={handlePredict}>

            <div className="form-grid">

              {/* Patient Age */}

              <div className="form-group">

                <label>Patient Age</label>

                <input
                  type="number"
                  name="patient_age"
                  value={formData.patient_age}
                  onChange={handleChange}
                  placeholder="Enter patient age"
                  required
                />

              </div>


              {/* Claim Amount */}

              <div className="form-group">

                <label>Claim Amount</label>

                <input
                  type="number"
                  name="claim_amount"
                  value={formData.claim_amount}
                  onChange={handleChange}
                  placeholder="Enter claim amount"
                  required
                />

              </div>


              {/* Eligibility */}

              <div className="form-group">

                <label>Eligibility</label>

                <select
                  name="eligibility"
                  value={formData.eligibility}
                  onChange={handleChange}
                  required
                >

                  <option value="">
                    Select eligibility
                  </option>

                  <option value="1">
                    Eligible
                  </option>

                  <option value="0">
                    Not Eligible
                  </option>

                </select>

              </div>


              {/* Prior Authorization */}

              <div className="form-group">

                <label>Prior Authorization</label>

                <select
                  name="prior_authorization"
                  value={formData.prior_authorization}
                  onChange={handleChange}
                  required
                >

                  <option value="">
                    Select authorization
                  </option>

                  <option value="1">
                    Approved
                  </option>

                  <option value="0">
                    Not Approved
                  </option>

                </select>

              </div>


              {/* Documentation */}

              <div className="form-group">

                <label>Documentation</label>

                <select
                  name="documentation"
                  value={formData.documentation}
                  onChange={handleChange}
                  required
                >

                  <option value="">
                    Select documentation
                  </option>

                  <option value="1">
                    Complete
                  </option>

                  <option value="0">
                    Incomplete
                  </option>

                </select>

              </div>


              {/* Claim Complexity */}

              <div className="form-group">

                <label>Claim Complexity</label>

                <input
                  type="number"
                  name="claim_complexity"
                  value={formData.claim_complexity}
                  onChange={handleChange}
                  step="0.01"
                  min="0"
                  max="1"
                  placeholder="Example: 0.75"
                  required
                />

              </div>


              {/* Historical Denial Rate */}

              <div className="form-group full-width">

                <label>
                  Historical Denial Rate
                </label>

                <input
                  type="number"
                  name="historical_denial_rate"
                  value={formData.historical_denial_rate}
                  onChange={handleChange}
                  step="0.01"
                  min="0"
                  max="1"
                  placeholder="Example: 0.60"
                  required
                />

              </div>

            </div>


            {/* PREDICT BUTTON */}

            <button
              type="submit"
              className="predict-btn"
              disabled={loading}
            >

              {loading
                ? "Predicting..."
                : "Predict Claim"}

            </button>

          </form>


          {/* ERROR */}

          {error && (
            <div className="error-box">
              {error}
            </div>
          )}

        </main>
      )}


      {/* RESULT DASHBOARD */}

      {result && (
        <main className="result-card">

          {/* RESULT HEADER */}

          <div className="result-header">

            <span className="result-icon">
              AI
            </span>

            <h2>
              Prediction Result
            </h2>

            <p>
              AI-powered medical claim assessment
            </p>

          </div>


          {/* PROBABILITY */}

          <div className="probability-section">

            <span className="probability-label">
              Denial Probability
            </span>

            <div
              className={
                result.risk_level === "HIGH"
                  ? "probability-value probability-high"
                  : "probability-value probability-low"
              }
            >
              {result.denial_probability}%
            </div>


            {/* PROGRESS BAR */}

            <div className="probability-bar">

              <div
                className={
                  result.risk_level === "HIGH"
                    ? "probability-fill high"
                    : "probability-fill low"
                }
                style={{
                  width: `${result.denial_probability}%`,
                }}
              ></div>

            </div>

          </div>


          {/* RESULT DETAILS */}

          <div className="result-details">

            {/* RISK LEVEL */}

            <div className="result-item">

              <span>
                Risk Level
              </span>

              <strong
                className={
                  result.risk_level === "HIGH"
                    ? "risk-high"
                    : "risk-low"
                }
              >
                {result.risk_level}
              </strong>

            </div>


            {/* DECISION */}

            <div className="result-item">

              <span>
                Decision
              </span>

              <strong
                className={
                  result.risk_level === "HIGH"
                    ? "decision-denied"
                    : "decision-approved"
                }
              >
                {result.decision}
              </strong>

            </div>

          </div>


          {/* CLAIM INFORMATION */}

          <div className="claim-summary">

            <h3>
              Claim Information
            </h3>

            <div className="summary-grid">

              <div className="summary-item">
                <span>
                  Patient Age
                </span>

                <strong>
                  {formData.patient_age}
                </strong>
              </div>


              <div className="summary-item">
                <span>
                  Claim Amount
                </span>

                <strong>
                  ₹{formData.claim_amount}
                </strong>
              </div>


              <div className="summary-item">
                <span>
                  Eligibility
                </span>

                <strong>
                  {formData.eligibility === "1"
                    ? "Eligible"
                    : "Not Eligible"}
                </strong>
              </div>


              <div className="summary-item">
                <span>
                  Prior Authorization
                </span>

                <strong>
                  {formData.prior_authorization === "1"
                    ? "Approved"
                    : "Not Approved"}
                </strong>
              </div>


              <div className="summary-item">
                <span>
                  Documentation
                </span>

                <strong>
                  {formData.documentation === "1"
                    ? "Complete"
                    : "Incomplete"}
                </strong>
              </div>


              <div className="summary-item">
                <span>
                  Claim Complexity
                </span>

                <strong>
                  {formData.claim_complexity}
                </strong>
              </div>


              <div className="summary-item">
                <span>
                  Historical Denial Rate
                </span>

                <strong>
                  {formData.historical_denial_rate}
                </strong>
              </div>

            </div>

          </div>


          {/* NEW PREDICTION */}

          <button
            className="new-prediction-btn"
            onClick={handleNewPrediction}
          >
            New Prediction
          </button>

        </main>
      )}

    </div>
  );
}

export default App;