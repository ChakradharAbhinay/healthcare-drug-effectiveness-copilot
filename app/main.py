from fastapi import FastAPI

from app.routers import health

app = FastAPI(
    title="Healthcare Drug Effectiveness Copilot",
    description="A healthcare AIML project using supervised ML, RAG, and fine-tuning exploration.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Healthcare Drug Effectiveness Copilot API is running"
    }


app.include_router(health.router)
