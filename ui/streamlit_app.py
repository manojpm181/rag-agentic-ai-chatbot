import sys
import os

# Add project root to Python path (CRITICAL)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import streamlit as st
from app.rag_graph import build_rag_graph


st.set_page_config(page_title="Agentic AI RAG Chatbot", layout="wide")

# Custom CSS for animations and styling
st.markdown("""
<style>
body {
    background: #0f172a;
    color: #e0e0e0;
    font-family: 'Montserrat', sans-serif;
}
h1, h2, h3 { color: #facc15; }
.chat-bubble {
    padding: 15px;
    border-radius: 15px;
    margin: 5px 0;
    animation: fadeIn 0.7s ease-in;
}
.user { background: #1e293b; text-align: right; }
.ai { background: #facc15; color: #0f172a; text-align: left; }
.progress-bar {
    background: linear-gradient(90deg, #facc15, #fcd34d);
    height: 10px;
    border-radius: 5px;
    animation: grow 1s ease-out forwards;
}
@keyframes fadeIn { from {opacity:0;} to {opacity:1;} }
@keyframes grow { from {width:0%} to {width:100%} }
button:hover { background: #fcd34d; color: #0f172a; }
</style>
""", unsafe_allow_html=True)

st.title("🤖 Agentic AI RAG Chatbot")
st.caption("Answers strictly grounded in the Agentic AI eBook")

rag_graph = build_rag_graph()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

question = st.text_input("Ask a question about Agentic AI:")

if st.button("Ask") and question:
    with st.spinner("AI is thinking... 🤖"):
        result = rag_graph.invoke({"question": question})
    answer = result.get("answer") or "No answer available"
    confidence = result.get("confidence") or 0.0
    st.session_state.chat_history.append({
        "question": question, "answer": answer,
        "confidence": confidence, "documents": result.get("documents", [])
    })

# Display chat history in animated bubbles
for chat in reversed(st.session_state.chat_history):
    st.markdown(f"<div class='chat-bubble user'>{chat['question']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='chat-bubble ai'>{chat['answer']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='progress-bar' style='width:{chat['confidence']*100}%'></div>", unsafe_allow_html=True)

    with st.expander("📄 Retrieved Context"):
        for i, doc in enumerate(chat.get("documents", [])):
            page = doc.metadata.get("page", "N/A") if hasattr(doc, "metadata") else "N/A"
            st.markdown(f"**Chunk {i+1} (page {page}):**")
            st.write(doc.page_content)
