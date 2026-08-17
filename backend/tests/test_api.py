from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"


def test_predict_claim():
    payload = {
        "patient_age": 55,
        "claim_amount": 1500,
        "eligibility": 1,
        "prior_authorization": 0,
        "documentation": 0,
        "claim_complexity": 0.75,
        "historical_denial_rate": 0.60,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "denial_probability" in data
    assert "risk_level" in data
    assert "decision" in data

    assert 0 <= data["denial_probability"] <= 100

    assert data["risk_level"] in ["HIGH", "LOW"]

    assert data["decision"] in [
        "CLAIM LIKELY TO BE DENIED",
        "CLAIM LIKELY TO BE APPROVED",
    ]