import pandas as pd
from pathlib import Path


# =========================
# FILE PATHS
# =========================

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_FILE = BASE_DIR / "data" / "raw" / "medical_claims.csv"

PROCESSED_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "medical_claims_processed.csv"
)


# =========================
# LOAD RAW DATASET
# =========================

df = pd.read_csv(RAW_FILE)

print("Original dataset shape:", df.shape)


# =========================
# MODEL FEATURES
# =========================

features = [
    "patient_age",
    "claim_amount",
    "eligibility",
    "prior_authorization",
    "documentation",
    "claim_complexity",
    "historical_denial_rate",
]


# =========================
# CREATE PROCESSED DATASET
# =========================

processed_df = df[features + ["claim_status"]].copy()


# =========================
# REMOVE MISSING VALUES
# =========================

processed_df = processed_df.dropna()


# =========================
# CREATE TARGET COLUMN
# =========================

processed_df["denial"] = (
    processed_df["claim_status"]
    .map({
        "Approved": 0,
        "Denied": 1
    })
)


# =========================
# SAVE PROCESSED DATASET
# =========================

PROCESSED_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

processed_df.to_csv(
    PROCESSED_FILE,
    index=False
)


# =========================
# DISPLAY INFORMATION
# =========================

print("Processed dataset shape:", processed_df.shape)

print("\nClass distribution:")
print(processed_df["claim_status"].value_counts())

print("\nProcessed file created:")
print(PROCESSED_FILE)