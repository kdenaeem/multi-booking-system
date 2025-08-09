from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

app = FastAPI()

load_dotenv()

app = FastAPI(
    title="Whatsapp Agent API",
    description="API for managing Whatsapp Agent operations",
    version="1.0.0",
)

sessions = {}
conversation_history = {}


class ChatMessage(BaseModel):
    phone_number: str
    message: str
    type: str
    content: str
    session_id: Optional[str] = None
    timestamp: Optional[str] = None


class ChatResponse(BaseModel):
    response_message: str
    session_id: Optional[str] = None
    intent: Optional[str] = None


@app.get("/")
async def root():
    return {"message": "Whatsapp Agent is running!"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.post("/test-message")
async def test_message(message_str):
    return {
        "received": message_str,
        "response": "This would be sent back to Whatsapp",
    }


@app.post("/process-message")
async def process_message(message: ChatMessage):

    session_id = (
        message.session_id
        or f"session_{message.phone_number}_{message.timestamp}"
    )

    if session_id not in sessions:
        sessions[session_id] = {
            "phone_number": message.phone_number,
            "created_at": datetime.now(),
            "messages": [],
        }
        conversation_history[session_id] = []

    conversation_history[session_id].append(
        {
            "message": message.message,
            "type": message.type,
            "content": message.content,
            "timestamp": message.timestamp or datetime.now().isoformat(),
        }
    )

    respose = await agent_processing(message, session_id)

    return respose


async def agent_processing(
    message: ChatMessage, session_id: str
) -> ChatResponse:
    # Simulate processing the message and generating a response
    response_message = f"Processed message: {message.message}"

    # Here you would typically call your agent logic, e.g., OpenAI API, etc.
    # For now, we return a mock response
    return ChatResponse(
        response_message=response_message,
        session_id=session_id,
        intent="mock_intent",
    )
