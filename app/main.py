from fastapi import FastAPI

app = FastAPI(
    title="Healthcare Drug Effectiveness Copilot",
    description="A healthcare AIML project using supervised ML, RAG, and fine-tuning exploration.",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Healthcare Drug Effectiveness Copilot API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "healthcare-drug-effectiveness-copilot"
    }

