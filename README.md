# Healthcare Drug Effectiveness Copilot

This project is an AIML healthcare application that combines:

1. Supervised Machine Learning
2. Retrieval Augmented Generation (RAG)
3. Fine-tuning exploration

## Project Idea

The system predicts drug effectiveness or rating from patient drug reviews using supervised machine learning.

Later, it will answer medicine-related questions using official FDA drug label information through RAG.

## Current Scope

- Build a basic FastAPI application
- Add a health check endpoint
- Explore UCI Drug Review dataset
- Train a model to predict drug rating/effectiveness
- Use FDA Metformin label data for RAG
- Explore MedQuAD dataset for fine-tuning

## Tech Stack

- Python
- FastAPI
- Scikit-learn
- Pandas
- Sentence Transformers
- FAISS or ChromaDB
- Hugging Face datasets

# Healthcare Drug Effectiveness Copilot

## Project Overview

Healthcare Drug Effectiveness Copilot is an AIML healthcare project that combines traditional supervised machine learning, Retrieval Augmented Generation (RAG), and fine-tuning exploration.

The first goal is to predict drug effectiveness from patient drug reviews. The project uses structured drug review data for supervised machine learning and later uses FDA drug label information for RAG-based question answering.

## Problem Statement

Patients write reviews about medicines based on their personal experiences. These reviews often contain useful signals about drug effectiveness, side effects, and overall satisfaction.

This project aims to:

- Analyze drug review data
- Predict drug rating or effectiveness class from review text
- Build a FastAPI service for ML prediction
- Use FDA drug label documents for RAG-based medical information retrieval
- Explore fine-tuning using healthcare Q&A data

## Current Project Architecture

```text
User / Client
    |
    v
FastAPI Application
    |
    |-- Health Endpoint
    |
    |-- ML Prediction Endpoint        [Planned]
    |
    |-- RAG Query Endpoint            [Planned]
    |
    |-- Fine-tuned Model Endpoint     [Planned]
    |
    v
Services Layer
    |
    |-- Data Processing
    |-- ML Model Inference
    |-- RAG Retrieval
    |-- LLM / Fine-tuned Model Logic
    |
    v
Data Layer
    |
    |-- Structured Drug Review Dataset
    |-- FDA Drug Label Documents
    |-- Postgres / PGVector            [Planned]

Architecture Diagram Placeholder

A final architecture diagram will be added later showing:

Gradio UI
FastAPI backend
ML model
RAG pipeline
Postgres / PGVector database
Fine-tuned model
Agent orchestration layer
Observability and logging
Tech Stack

Current tools:

Python
FastAPI
Uvicorn
Pandas
NumPy
Scikit-learn
Pre-commit
Black
Ruff
Isort

Planned tools:

Postgres
PGVector
MLflow or Weights & Biases
Hugging Face Transformers
LoRA / QLoRA
Gradio
Docker
GitHub Actions
Project Structure
healthcare-drug-effectiveness-copilot/
│
├── app/
│   ├── main.py
│   ├── routers/
│   ├── models/
│   ├── services/
│   └── schemas/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── ml/
│   ├── saved_models/
│   └── 01_explore_drug_reviews.py
│
├── rag/
│   └── documents/
│
├── tests/
│
├── requirements.txt
├── .pre-commit-config.yaml
├── .gitignore
└── README.md

### Setup Instructions
git clone git@github-school:ChakradharAbhinay/healthcare-drug-effectiveness-copilot.git
cd healthcare-drug-effectiveness-copilot
2. Activate Python environment

This project currently uses the existing Conda environment:
conda activate longchain_envllm
3. Install dependencies
python -m pip install -r requirements.txt
4. Install pre-commit hooks
python -m pre_commit install
5. Run pre-commit checks manually
python -m pre_commit run --all-files
Running the FastAPI Application

Start the API server:
python -m uvicorn app.main:app --reload
Open the API in browser:
http://127.0.0.1:8000
Health endpoint:
http://127.0.0.1:8000/health
Swagger documentation:
http://127.0.0.1:8000/docs
Current API Endpoints
Root Endpoint
GET /
Health Endpoint
GET /health
{
  "status": "ok",
  "service": "healthcare-drug-effectiveness-copilot"
}
Dataset
Structured Dataset

The structured dataset used for supervised ML is the UCI Drug Review dataset from Kaggle.

Local files:
data/raw/drugsComTrain_raw.csv
data/raw/drugsComTest_raw.csv

These raw dataset files are not committed to GitHub because they are ignored in .gitignore.
Dataset columns:

uniqueID
drugName
condition
review
rating
date
usefulCount

Initial ML target:

rating

Initial ML input features:

review
drugName
condition
usefulCount
Unstructured Dataset

The unstructured dataset planned for RAG is the FDA drug label information for Metformin.

Source:

FDA Drug Label API for Metformin

Planned RAG use case:

User asks a question about Metformin.
The system retrieves relevant FDA label content.
The system returns a grounded answer with sources.
Fine-tuning Dataset

The planned fine-tuning dataset is MedQuAD.

Planned use case:

Healthcare question-answering fine-tuning exploration.




