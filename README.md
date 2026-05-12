# 🚀 AI Career Prediction Engine

## Overview
The AI Career Prediction Engine is an intelligent recommendation system designed to match aspiring technologists with optimal roles in the Artificial Intelligence and Data Science ecosystem. 

By analyzing a user's programming level, domain interests (Data, Text, Images), and preferred work style (Analysis, Modeling, Research), this system provides targeted career guidance, recommending roles ranging from **Data Analyst** to **Computer Vision Engineer** and **AI Generalist**.

## 🧠 System Architecture
This project demonstrates the evolution from a deterministic rule-based engine to a scalable Machine Learning pipeline.

1. **Rule-Based Prototype (`ai_career_profile.py`):** An interactive command-line application that uses control-flow logic to instantly map user inputs to career profiles. Great for lightweight, deterministic recommendations.
2. **Machine Learning Pipeline (`ai_career_ML.py`):** A predictive model utilizing a `DecisionTreeClassifier` from Scikit-Learn. It learns from historical mapped data (`career_data.csv`) to infer the best career path based on non-linear patterns in user attributes.

## 🛠️ Technology Stack
* **Language:** Python 3.x
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Decision Trees)

## 📂 Repository Structure
```text
├── career_data.csv          # Structured dataset mapping inputs to career roles
├── ai_career_profile.py     # Interactive rule-based recommendation script
├── ai_career_ML.py          # Machine learning classification pipeline
└── README.md                # Project documentation
