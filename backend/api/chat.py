"""
backend/api/chat.py — Portfolio Chatbot Endpoint

Exposes POST /api/chat, matching ChatWidget.jsx:
  request:  { "question": "..." }
  response: { "answer": "...", "sources": ["resume.pdf", "projects.txt"] }
"""

from __future__ import annotations

import traceback
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

# Fallback import handling to support both local running and Vercel serverless execution
try:
    from backend.rag.pipeline import answer_question
except ModuleNotFoundError:
    try:
        from rag.pipeline import answer_question
    except ModuleNotFoundError:
        import os
        import sys

        sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        from backend.rag.pipeline import answer_question

router = APIRouter()


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=1000)


class ChatResponse(BaseModel):
    answer: str
    sources: list[str] = Field(default_factory=list)


@router.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest) -> ChatResponse:
    question = payload.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    try:
        result = answer_question(question)
        return ChatResponse(
            answer=result.get("answer", "No response generated."),
            sources=result.get("sources", []),
        )
    except RuntimeError as e:
        # Triggered if API key is missing or model configuration fails
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Failed to answer question: {str(e)}")