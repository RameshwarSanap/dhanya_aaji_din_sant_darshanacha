from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(
    title="Medical Claim AI",
    description="AI-Based Medical Claim Approval and Denial Prediction System",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
        "http://localhost:5176",
        "http://127.0.0.1:5176",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Load trained ML model
model = joblib.load("ml/models/denial_model.pkl")


class ClaimRequest(BaseModel):
    patient_age: int
    claim_amount: float
    eligibility: int
    prior_authorization: int
    documentation: int
    claim_complexity: float
    historical_denial_rate: float


@app.get("/")
def home():
    return {
        "message": "Medical Claim AI API is running!",
        "status": "success"
    }


@app.post("/predict")
def predict_claim(claim: ClaimRequest):

    data = pd.DataFrame([{
        "patient_age": claim.patient_age,
        "claim_amount": claim.claim_amount,
        "eligibility": claim.eligibility,
        "prior_authorization": claim.prior_authorization,
        "documentation": claim.documentation,
        "claim_complexity": claim.claim_complexity,
        "historical_denial_rate": claim.historical_denial_rate
    }])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    if prediction == 1:
        risk_level = "HIGH"
        decision = "CLAIM LIKELY TO BE DENIED"
    else:
        risk_level = "LOW"
        decision = "CLAIM LIKELY TO BE APPROVED"

    return {
        "denial_probability": round(float(probability) * 100, 2),
        "risk_level": risk_level,
        "decision": decision
    }