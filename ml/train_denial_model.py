import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
# Load dataset
df = pd.read_csv("data/raw/medical_claims.csv")

# Convert target
df["target"] = df["claim_status"].map({
    "Approved": 0,
    "Denied": 1
})
# Select features
features = [
    "patient_age",
    "claim_amount",
    "eligibility",
    "prior_authorization",
    "documentation",
    "claim_complexity",
    "historical_denial_rate"
]

X = df[features]
y = df["target"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Dataset loaded successfully!")
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
print("Features:", features)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Create Logistic Regression model
model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Training Complete!")
print("Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# Save trained model
model_path = "ml/models/denial_model.pkl"

joblib.dump(model, model_path)

print("\nModel saved successfully!")
print("Saved at:", model_path)