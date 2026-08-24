from fastapi import FastAPI
from pydantic import BaseModel

from app.agent import agent


app = FastAPI(
    title="Agentic RAG Assistant",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():

    return {
        "message": "Agentic RAG Assistant API"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    result = agent.invoke(
        {
            "question": request.question,
            "context": "",
            "answer": ""
        }
    )

    return {
        "question": request.question,
        "answer": result["answer"]
    }
