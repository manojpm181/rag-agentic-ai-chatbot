from typing import List
from langchain_core.documents import Document

def retrieve_documents(question: str, **kwargs) -> List[Document]:
    """
    Returns documents only if the question is about Agentic AI.
    Otherwise, returns an empty list to trigger "not available".
    """
    top_k = kwargs.get("top_k", 4)
    q = question.lower().strip()

    # Keywords indicating Agentic AI domain
    agentic_keywords = ["agentic ai", "agentic", "ai systems", "planning", "reasoning", "goals", "memory", "execution"]
    
    if not any(keyword in q for keyword in agentic_keywords):
        # Out-of-scope → no documents
        return []

    # Agentic AI document chunks
    docs = [
        Document(page_content="Agentic AI systems can plan, reason, and act autonomously."),
        Document(page_content="Unlike traditional AI, Agentic AI proactively achieves goals."),
        Document(page_content="Agentic AI combines memory, reasoning, and action execution."),
    ]

    return docs[:top_k]
