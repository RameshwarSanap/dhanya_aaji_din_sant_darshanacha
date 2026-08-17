import pandas as pd
import numpy as np

np.random.seed(42)

# Number of synthetic claims
N = 10000

# Generate synthetic medical claim data
data = {
    "claim_id": [f"C{10000 + i}" for i in range(N)],
    "patient_age": np.random.randint(18, 85, N),
    "diagnosis": np.random.choice(
        ["Diabetes", "Hypertension", "Asthma", "Heart Disease", "Arthritis"],
        N
    ),
    "icd_code": np.random.choice(
        ["E11.9", "I10", "J45.909", "I25.10", "M19.90"],
        N
    ),
    "cpt_code": np.random.choice(
        ["99213", "99214", "99215", "93000", "80053"],
        N
    ),
    "payer_id": np.random.choice(
        ["P001", "P002", "P003", "P004", "P005"],
        N
    ),
    "claim_amount": np.round(
        np.random.uniform(100, 2000, N), 2
    ),
    "eligibility": np.random.choice([0, 1], N, p=[0.10, 0.90]),
    "prior_authorization": np.random.choice([0, 1], N, p=[0.30, 0.70]),
    "documentation": np.random.choice([0, 1], N, p=[0.20, 0.80]),
    "claim_complexity": np.round(
        np.random.uniform(0, 1, N), 2
    ),
    "historical_denial_rate": np.round(
        np.random.uniform(0, 1, N), 2
    )
}

# Create DataFrame
df = pd.DataFrame(data)

# Create a synthetic denial probability
risk_score = (
    0.30 * (1 - df["eligibility"])
    + 0.20 * (1 - df["prior_authorization"])
    + 0.20 * (1 - df["documentation"])
    + 0.15 * df["claim_complexity"]
    + 0.15 * df["historical_denial_rate"]
)

# Convert risk into synthetic claim status
df["denial_probability"] = np.round(risk_score, 2)

df["claim_status"] = np.where(
    df["denial_probability"] >= 0.50,
    "Denied",
    "Approved"
)

# Save dataset
output_path = "data/raw/medical_claims.csv"
df.to_csv(output_path, index=False)

print("Dataset generated successfully!")
print(f"Total claims: {len(df)}")
print(f"Saved to: {output_path}")
print("\nFirst 5 records:")
print(df.head())