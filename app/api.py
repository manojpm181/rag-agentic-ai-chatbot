from fastapi import FastAPI
from pydantic import BaseModel
from .rag_graph import build_rag_graph

app = FastAPI(
    title="Agentic AI RAG Chatbot",
    description="RAG-based chatbot grounded in Agentic AI eBook",
    version="1.0"
)

rag_graph = build_rag_graph()

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str
    confidence: float
    context: list[str]

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    result = rag_graph.invoke({
        "question": request.question
    })

    context_chunks = []
    if "documents" in result:
        context_chunks = [doc.page_content for doc in result["documents"]]

    return ChatResponse(
        answer=result["answer"],
        confidence=result["confidence"],
        context=context_chunks
    )
