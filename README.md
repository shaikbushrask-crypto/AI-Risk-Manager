# AI Risk Manager

AI Risk Manager is an explainable behavioral risk analysis web application built with Python and Flask.

The system analyzes transaction behavior using spending patterns, device trust, transaction speed, historical behavior, and Risk DNA to generate an understandable risk decision.

---

## Project Overview

AI Risk Manager is designed to detect unusual behavioral changes during transaction analysis.

Instead of showing only a risk score, the system explains:

- Why the transaction is risky
- Which factors contributed to the risk
- How much the behavior changed
- What would happen if a risk factor changed
- How the current behavior compares with previous behavior
- How the user's Risk DNA evolves over time

The project focuses on **behavioral analysis and explainability**.

---

## Key Features

### 1. Risk DNA Analysis

The system calculates a behavioral risk score based on three major signals:

- Spending behavior
- Device behavior
- Transaction speed

Risk levels:

- NORMAL
- WARNING
- CRITICAL

Example:

Risk Score: 90/90  
Risk Level: CRITICAL

---

### 2. Risk Mutation

Risk Mutation identifies how significantly the current behavior has changed.

Possible mutation levels:

- NORMAL
- SLIGHT CHANGE
- MAJOR CHANGE
- CRITICAL CHANGE

This helps identify sudden behavioral changes.

---

### 3. Behavioral Mirror

Behavioral Mirror compares the user's normal behavior with the current transaction.

It analyzes:

- Normal spending vs current spending
- Trusted device vs new device
- Normal transaction speed vs rapid transactions

Example:

Normal Spending: ₹5,000  
Current Spending: ₹40,000  
Change: +700%

---

### 4. Counterfactual Risk Analysis

The system checks alternative situations to understand which factors are responsible for the risk.

Examples:

- If transaction amount was normal
- If a trusted device was used
- If amount and device were normal

This improves the explainability of the risk decision.

---

### 5. What-If Risk Simulator

The What-If Risk Simulator allows different behavioral conditions to be tested.

Scenarios include:

- Current Behavior
- What if amount was normal?
- What if trusted device was used?
- What if transaction speed was normal?
- What if all behavior was normal?

This shows how the risk score changes under different conditions.

---

### 6. Risk Decision Explanation

The system automatically explains why a particular risk decision was generated.

For example:

The transaction amount is significantly higher than the user's normal spending pattern.

The transaction is being performed from a new device instead of a trusted device.

Multiple transactions are occurring at an unusually rapid speed.

The system then provides a final action:

- ALLOW TRANSACTION
- VERIFY USER
- BLOCK / MANUAL REVIEW

---

### 7. Risk Confidence

The system evaluates the number of unusual behavioral signals and generates a confidence level.

Possible levels:

- VERY LOW
- LOW
- MEDIUM
- HIGH

---

### 8. Risk Pattern Classification

The system classifies the overall behavioral pattern.

Possible patterns:

- NORMAL BEHAVIOR PATTERN
- MINOR BEHAVIOR CHANGE
- SUSPICIOUS BEHAVIOR PATTERN
- HIGH-RISK BEHAVIOR PATTERN

It also identifies individual behavioral patterns such as:

- HIGH SPENDING CHANGE
- MODERATE SPENDING CHANGE
- NEW DEVICE
- RAPID TRANSACTION ACTIVITY
- TRUSTED DEVICE
- NORMAL TRANSACTION SPEED

---

### 9. Risk Factor Contribution

The system shows how each factor contributes to the final risk score.

Example:

Spending: +35 points  
New Device: +25 points  
Rapid Transactions: +30 points

This makes the decision transparent.

---

### 10. Risk DNA Fingerprint

The system creates a compact behavioral fingerprint based on:

- Spending
- Device
- Transaction Speed

Example:

HIGH-NEW-RAPID

This represents:

Spending: HIGH  
Device: NEW  
Transaction Speed: RAPID

The fingerprint provides a simple way to represent the user's current behavioral pattern.

---

### 11. Risk DNA Similarity

The current Risk DNA is compared with the previous Risk DNA.

The system identifies:

- DNA Similarity
- Similarity Level
- Changed Components

Example:

DNA Similarity: 67%

Changed Component:

- SPENDING

---

### 12. Risk DNA Behavioral Memory

The system stores previous behavioral patterns during the application session.

It identifies the user's dominant historical Risk DNA.

Example:

Current Behavioral DNA:

HIGH-TRUSTED-NORMAL

Dominant Historical DNA:

NORMAL-TRUSTED-NORMAL

The system can identify whether the current behavior is:

BEHAVIOR CONSISTENT

or

BEHAVIORAL MEMORY CHANGE

---

### 13. Risk DNA Evolution Score

The system measures how much the user's behavioral DNA has changed compared with the previous analysis.

Possible results:

- NO CHANGE
- MINOR EVOLUTION
- MAJOR EVOLUTION
- SIGNIFICANT EVOLUTION

Example:

Evolution Score: 33%

Change Level:

MINOR EVOLUTION

Changed Component:

SPENDING

---

### 14. Risk Trend Analysis

The system compares the current risk score with the previous analysis.

Possible results:

- RISK INCREASING
- RISK DECREASING
- RISK STABLE
- NOT ENOUGH DATA

This helps track whether risk is increasing or decreasing.

---

### 15. Risk DNA Change Timeline

The system tracks Risk DNA changes across multiple analyses.

Example:

Analysis #1

Risk Score: 0/90  
Direction: BASELINE

Analysis #2

Risk Score: 35/90  
Direction: RISK INCREASED

This provides a simple view of behavioral evolution.

---

### 16. Risk Analysis History

The system maintains previous risk analyses during the application session.

The history contains:

- Risk Score
- Risk Level
- Risk Mutation
- Recommended Action
- Confidence
- Risk DNA Fingerprint

This allows current behavior to be compared with previous behavior.

---

# Risk Scoring System

The current Risk DNA engine uses three major behavioral signals.

## Spending

If the transaction amount is more than 3 times the usual amount:

+35 points

If the transaction amount is more than 1.5 times the usual amount:

+20 points

---

## New Device

If the transaction is performed using a new device:

+25 points

---

## Rapid Transactions

If transactions are occurring rapidly:

+30 points

---

## Maximum Risk Score

90/90

---

# Risk Levels

0–34

NORMAL

35–69

WARNING

70–90

CRITICAL

---

# Recommended Actions

0–34

ALLOW TRANSACTION

35–69

VERIFY USER

70–90

BLOCK / MANUAL REVIEW

---

# Risk Analysis Architecture

The application follows this behavioral analysis flow:

User Transaction

↓

Transaction Behavioral Signals

↓

Spending Analysis

↓

Device Analysis

↓

Transaction Speed Analysis

↓

Risk Score

↓

Risk Level

↓

Risk Mutation

↓

Risk Confidence

↓

Risk Pattern Classification

↓

Risk Factor Contribution

↓

Behavioral Mirror

↓

Counterfactual Risk

↓

What-If Risk Simulation

↓

Risk DNA Fingerprint

↓

Risk DNA Similarity

↓

Behavioral Memory

↓

Risk DNA Evolution

↓

Risk Trend

↓

Risk DNA Timeline

↓

Explainable Risk Decision

---

# Example: Normal Transaction

Usual Amount:

₹5,000

Current Amount:

₹6,000

Device:

Trusted Device

Transaction Speed:

Normal

Result:

Risk Score: 0/90

Risk Level: NORMAL

Recommended Action:

ALLOW TRANSACTION

Risk DNA:

NORMAL-TRUSTED-NORMAL

---

# Example: High-Risk Transaction

Usual Amount:

₹5,000

Current Amount:

₹40,000

Device:

New Device

Transaction Speed:

Rapid

Result:

Risk Score: 90/90

Risk Level: CRITICAL

Recommended Action:

BLOCK / MANUAL REVIEW

Risk DNA:

HIGH-NEW-RAPID

---

# Explainability

One of the main goals of this project is explainability.

Instead of returning only:

Risk Score: 90

the system provides additional information:

- Why the risk is high
- Which behavioral factors contributed
- How much behavior changed
- What the risk would be under different conditions
- How similar the current Risk DNA is to previous behavior
- Which Risk DNA components changed
- How behavior evolved
- Whether risk is increasing or decreasing

This makes the risk decision easier to understand.

---

# Technology Stack

## Backend

Python

Flask

## Frontend

HTML

CSS

JavaScript

---

# Project Structure

AI-Risk-Manager/

├── app.py

├── risk_engine.py

└── templates/

    └── index.html

---

# Main Files

## app.py

The Flask application that:

- Receives user input
- Calls the risk engine
- Performs risk analysis
- Maintains analysis history
- Sends results to the frontend

---

## risk_engine.py

Contains the core behavioral risk analysis functions.

Major components include:

- calculate_risk_dna()
- calculate_mutation()
- behavioral_mirror()
- counterfactual_risk()
- risk_action()
- risk_explanation()
- risk_confidence()
- risk_pattern()
- risk_trend()
- risk_factor_contribution()
- what_if_risk()
- risk_change_timeline()
- risk_dna_fingerprint()
- risk_dna_similarity()
- risk_dna_memory()
- risk_dna_evolution()

---

## templates/index.html

The frontend interface of the AI Risk Manager.

It displays the risk analysis results and provides the user interface for interacting with the system.

---

# How to Run the Project

## 1. Clone the repository

```bash
git clone https://github.com/shaikbushrask-crypto/AI-Risk-Manager.git
2. Open the project folder
cd AI-Risk-Manager
3. Install Flask
pip install flask
4. Run the application
python app.py
5. Open in browser
http://127.0.0.1:5000
Project Objective

The main objective of AI Risk Manager is to demonstrate an explainable behavioral risk analysis system capable of:

Detecting unusual transaction behavior.
Calculating behavioral risk.
Identifying behavioral changes.
Explaining risk decisions.
Comparing current and historical Risk DNA.
Simulating alternative behavioral conditions.
Tracking behavioral evolution.
Providing transparent risk recommendations.
What Makes the Project Unique

The project combines multiple explainability and behavioral-analysis concepts into one system.

The important unique components are:

Risk DNA
Behavioral Fingerprint
Behavioral Mirror
Counterfactual Risk
What-If Risk Simulation
Risk DNA Similarity
Risk DNA Behavioral Memory
Risk DNA Evolution
Risk Mutation
Risk Trend
Risk DNA Change Timeline
Risk Factor Contribution
Explainable Risk Decision

Together, these components allow the system to analyze not only the current transaction but also the change in behavioral patterns.

Current Project Status

Functional Prototype

The current version implements the behavioral risk engine and explainability modules using Python, Flask, HTML, CSS, and JavaScript.

Future Scope

Future versions can include:

Persistent database storage
User authentication
Real-time transaction monitoring
Machine learning-based risk prediction
Advanced anomaly detection
Historical transaction datasets
Real-time alerts
API integration
Advanced analytics dashboard
Production deployment
Enterprise risk monitoring
Author

Thaiseen Nishath

B.Tech – Computer Science Engineering

Purpose

This project is developed as a final-year Computer Science Engineering project and portfolio project for demonstrating skills in:

Python
Flask
Web Application Development
Behavioral Risk Analysis
Explainable Systems
Data-driven Decision Making
Software Development
