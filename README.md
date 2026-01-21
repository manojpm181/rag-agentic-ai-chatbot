# 🤖 Agentic AI RAG Chatbot (LangGraph-based)

A **Retrieval-Augmented Generation (RAG)** chatbot built using **LangGraph**, **LangChain**, and **Vector Embeddings**, designed to answer questions **strictly grounded** in the *Agentic AI eBook*.

This project was developed as part of an **AI Engineer Intern interview task** for **Appening Infotech**.

---

## 📌 Key Features

- 📖 Ingests and indexes the *Agentic AI eBook* (PDF)
- 🔍 Semantic retrieval using vector similarity search
- 🧠 Agentic RAG pipeline implemented with **LangGraph**
- 🚫 Hallucination prevention via grounding checks
- 📊 Confidence score based on retrieval strength
- 🔎 Displays retrieved context for transparency
- 🌐 Accessible via **FastAPI API** and **Streamlit UI**

---

## 🏗️ Architecture Overview

User Question
↓
LangGraph State Machine
↓
[ Retrieve Node ]
↓
[ Grounding Check Node ]
↓
[ Answer Generator Node ]
↓
Final Answer + Retrieved Context + Confidence Score


---

## ⚙️ Tech Stack

- **Python** 3.10+
- **LangChain**
- **LangGraph**
- **ChromaDB** (Vector Store)
- **OpenAI Embeddings & Chat Models**
- **FastAPI**
- **Streamlit**

---

## 📂 Project Structure
rag-agentic-ai-chatbot/
│
├── app/
│ ├── ingest.py # PDF ingestion & embedding
│ ├── retriever.py # Vector DB loader & retriever
│ ├── rag_graph.py # LangGraph-based RAG pipeline
│ ├── api.py # FastAPI backend
│ └── init.py
│
├── ui/
│ └── streamlit_app.py # Streamlit chat UI
│
├── data/
│ └── Agentic-AI.pdf # Source document
│
├── requirements.txt
├── .env.example
└── README.md


---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd rag-agentic-ai-chatbot

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure Environment Variables

Create a .env file (do NOT commit this):

OPENAI_API_KEY=your_openai_api_key


A safe template is provided as .env.example.

4️⃣ Ingest the PDF
python app/ingest.py


This step:

Loads the PDF

Splits it into chunks

Generates embeddings

Stores them in the vector database

5️⃣ Run the FastAPI Backend
uvicorn app.api:app --reload


📘 Swagger UI available at:

http://127.0.0.1:8000/docs

6️⃣ Run the Streamlit UI
streamlit run ui/streamlit_app.py

🧪 Sample Queries

What is Agentic AI?

How does Agentic AI differ from traditional LLM pipelines?

What are the core components of an agentic system?

Why are tools and planning important in agentic architectures?

How does autonomy play a role in agent-based AI?

What limitations of LLMs does Agentic AI aim to address?

🧠 Design Decisions

LangGraph models the RAG workflow as a state machine, enabling clear reasoning flow and extensibility.

A grounding check node prevents hallucinated answers when no relevant context is retrieved.

ChromaDB was chosen for its simplicity and reliability during local development.

Chunking strategy (500 tokens with 100 overlap) balances semantic coherence and retrieval accuracy.

Confidence score is derived from retrieval strength for interpretability.

🚫 Limitations & Future Improvements

Improve confidence scoring using average embedding similarity

Add streaming responses and inline citations

Support multiple PDFs and document collections

Add authentication and usage logging

Deploy using Docker or Streamlit Cloud

✅ Conclusion

This project demonstrates a production-oriented Agentic RAG system with a strong focus on:

Correctness

Explainability

Modular, agent-based design

It showcases practical use of LangGraph for building reliable and extensible AI pipelines.

⚠️ Notes

venv/ and .env are intentionally excluded from version control

Environment variables must be set via .env (local) or platform secrets (deployment)


---

### ✅ This README is:
- GitHub-ready
- Interview-friendly
- Deployment-safe
- Cleanly structured
- Copy-paste usable

If you want next, I can:
- ⭐ Optimize this README for **ATS & recruiters**
- 🚀 Add **deployment section (Streamlit Cloud / HF Spaces)**
- 🐳 Create a **Dockerfile**
- 🧪 Add **evaluation metrics section**

Just tell me 👍
