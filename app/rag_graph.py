from typing import List, TypedDict
from langgraph.graph import StateGraph, END
from langchain_core.documents import Document
from .retriever import retrieve_documents

class RAGState(TypedDict):
    question: str
    documents: List[Document]
    answer: str
    confidence: float

def retrieve_node(state: RAGState):
    q = state["question"].lower().strip()

    # ✅ Flexible identity routing
    identity_triggers = [
        "who are you", "what are you", "who r you",
        "introduce yourself", "your name"
    ]
    if any(trigger in q for trigger in identity_triggers):
        return {
            "documents": [],
            "answer": "I am an Agentic AI RAG chatbot that answers questions strictly based on the Agentic AI eBook.",
            "confidence": 1.0,
        }

    # Otherwise, retrieve documents
    docs = retrieve_documents(state["question"])
    return {"documents": docs}


def generate_answer_node(state: RAGState):
    # ✅ If answer already exists (from routing), just return it
    if "answer" in state and state["answer"] is not None:
        if "confidence" not in state or state["confidence"] is None:
            state["confidence"] = 1.0
        return state

    docs = state.get("documents", [])

    # No documents found
    if not docs:
        return {
            "answer": "The information is not available in the provided document.",
            "confidence": 0.0,
        }

    # Combine text from documents
    combined_text = " ".join(doc.page_content for doc in docs)

    # Confidence = proportion of documents retrieved (capped at 1.0)
    confidence = min(1.0, len(docs) / 4)

    return {
        "answer": combined_text,
        "confidence": confidence,
    }

def build_rag_graph():
    graph = StateGraph(RAGState)
    graph.add_node("retrieve", retrieve_node)
    graph.add_node("generate_answer", generate_answer_node)
    graph.set_entry_point("retrieve")
    graph.add_edge("retrieve", "generate_answer")
    graph.add_edge("generate_answer", END)
    return graph.compile()
