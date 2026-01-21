# 🤖 Agentic AI RAG Chatbot (LangGraph-based)

A Retrieval-Augmented Generation (RAG) chatbot built using **LangGraph**, **LangChain**, and **Vector Embeddings**, designed to answer questions **strictly grounded** in the *Agentic AI eBook*.

This project was built as part of the **AI Engineer Intern interview task** for Appening Infotech.

---

## 📌 Key Features

- 📖 Ingests and indexes the *Agentic AI eBook* (PDF)
- 🔍 Retrieves relevant content using vector similarity search
- 🧠 Agentic RAG pipeline implemented with **LangGraph**
- 🚫 Hallucination prevention via grounding checks
- 📊 Confidence score based on retrieval strength
- 🔎 Shows retrieved context for transparency
- 🌐 Exposed via **FastAPI** and **Streamlit UI**

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
Final Answer + Context + Confidence


---

## ⚙️ Tech Stack

- Python 3.10+
- LangChain
- LangGraph
- ChromaDB (Vector Store)
- OpenAI Embeddings & Chat Models
- FastAPI
- Streamlit

---

## 📂 Project Structure

rag-agentic-ai-chatbot/
│
├── app/
│ ├── ingest.py # PDF ingestion & embedding
│ ├── retriever.py # Vector DB loader & retriever
│ ├── rag_graph.py # LangGraph RAG pipeline
│ ├── api.py # FastAPI backend
│
├── ui/
│ └── streamlit_app.py # Streamlit chat UI
│
├── data/
│ └── agentic_ai.pdf
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

3️⃣ Set Environment Variables

Create a .env file:

OPENAI_API_KEY=your_openai_key

4️⃣ Ingest the PDF
python app/ingest.py

5️⃣ Run the API
uvicorn app.api:app --reload


Swagger UI available at:

http://127.0.0.1:8000/docs

6️⃣ Run the UI
streamlit run ui/streamlit_app.py

🧪 Sample Queries

What is Agentic AI?

How does Agentic AI differ from traditional LLM pipelines?

What are the core components of an agentic system?

Why are tools and planning important in agentic architectures?

How does autonomy play a role in agent-based AI?

What limitations of LLMs does Agentic AI aim to address?

🧠 Design Decisions

LangGraph was used to model the RAG pipeline as a state machine, enabling clear reasoning flow and future extensibility.

A grounding check node prevents hallucinations when no relevant context is retrieved.

ChromaDB was selected for its simplicity and reliability during local development.

Chunking strategy (500 tokens with 100 overlap) balances semantic coherence and retrieval accuracy.

Confidence score is derived from retrieval strength for interpretability.

🚫 Limitations & Future Improvements

Confidence scoring can be enhanced using embedding similarity averages.

Streaming responses and citations can be added.

Support for multiple documents and PDFs.

✅ Conclusion

This project demonstrates a production-oriented RAG system with a focus on correctness, explainability, and agentic design principles.
#

