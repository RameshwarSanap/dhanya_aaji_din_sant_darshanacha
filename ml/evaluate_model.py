import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)


# =========================
# LOAD DATASET
# =========================

df = pd.read_csv("data/raw/medical_claims.csv")


# =========================
# CREATE TARGET
# =========================

df["target"] = df["claim_status"].map({
    "Approved": 0,
    "Denied": 1
})


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


X = df[features]
y = df["target"]


# =========================
# SAME TRAIN/TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# =========================
# LOAD TRAINED MODEL
# =========================

model = joblib.load("ml/models/denial_model.pkl")


# =========================
# TEST SET PREDICTION
# =========================

y_pred = model.predict(X_test)


# =========================
# CALCULATE METRICS
# =========================

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred,
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    zero_division=0
)

cm = confusion_matrix(y_test, y_pred)


# =========================
# DISPLAY RESULTS
# =========================

print("\n===================================")
print("       MEDICAL CLAIM AI")
print("       FINAL MODEL EVALUATION")
print("===================================")

print("\nTotal Dataset:", len(df))
print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))

print("\nAccuracy :", round(accuracy * 100, 2), "%")
print("Precision:", round(precision * 100, 2), "%")
print("Recall   :", round(recall * 100, 2), "%")
print("F1 Score :", round(f1 * 100, 2), "%")


# =========================
# CONFUSION MATRIX
# =========================

print("\nConfusion Matrix:")
print(cm)


# =========================
# CLASSIFICATION REPORT
# =========================

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=[
            "Approved",
            "Denied"
        ],
        zero_division=0
    )
)