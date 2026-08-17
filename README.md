# 🏥 Medical Claim AI

An AI-powered medical claim analysis and denial prediction system that predicts the likelihood of a medical insurance claim being denied.

The project combines Machine Learning, FastAPI, and React to provide an end-to-end full-stack AI application.

---

## 🚀 Project Overview

Medical insurance claims can be denied due to several factors such as:

- Patient eligibility
- Missing documentation
- Prior authorization
- Claim complexity
- Claim amount
- Historical denial patterns

This project uses Machine Learning to analyze these factors and estimate the probability that a claim will be denied.

---

## 🎯 Objectives

- Predict medical claim denial probability
- Identify high-risk claims
- Provide an automated claim risk assessment
- Build a full-stack AI application
- Provide a REST API for ML predictions
- Create an interactive web interface

---

## 🧠 Machine Learning

The current ML model uses the following features:

- Patient Age
- Claim Amount
- Eligibility
- Prior Authorization
- Documentation
- Claim Complexity
- Historical Denial Rate

### Dataset

A synthetic medical claim dataset containing:

- 10,000 medical claims
- 9,013 approved claims
- 987 denied claims

Dataset location:

```text
data/raw/medical_claims.csv
