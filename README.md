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

- Loads the PDF

- Splits it into chunks

- enerates embeddings

- Stores them in the vector database

5️⃣ Run the FastAPI Backend

    uvicorn app.api:app --reload

📘 Swagger UI available at:

    http://127.0.0.1:8000/docs

6️⃣ Run the Streamlit UI

    streamlit run ui/streamlit_app.py

https://manojpm181-rag-agentic-ai-chatbot-uistreamlit-app-ij4aln.streamlit.app/

🧪 Sample Queries

    What is Agentic AI?
    
    How does Agentic AI differ from traditional LLM pipelines?
    
    What are the core components of an agentic system?
    
    Why are tools and planning important in agentic architectures?
    
    How does autonomy play a role in agent-based AI?
    
    What limitations of LLMs does Agentic AI aim to address?

## 🧠 Design Decisions

- **LangGraph-based State Machine**  
  LangGraph is used to model the RAG workflow as a state machine, enabling a clear reasoning flow, modular node design, and easy future extensibility.

- **Grounding Check for Hallucination Prevention**  
  A dedicated grounding check node ensures that answers are generated only when relevant context is retrieved, reducing hallucinations.

- **ChromaDB as Vector Store**  
  ChromaDB was selected for its simplicity, reliability, and ease of use during local development and experimentation.

- **Chunking Strategy**  
  Documents are chunked into **500-token segments with 100-token overlap** to maintain semantic coherence while improving retrieval accuracy.

- **Confidence Scoring Mechanism**  
  A confidence score is computed based on retrieval strength, providing interpretability and transparency for each generated response.


## 🚫 Limitations & Future Improvements

- Enhance confidence scoring using average embedding similarity metrics
- Add streaming responses for real-time answer generation
- Include inline citations for better traceability and trust
- Support multiple PDFs and document collections
- Add authentication and usage logging
- Deploy using Docker or Streamlit Cloud for scalable production use

---

## ✅ Conclusion

This project demonstrates a **production-oriented Agentic RAG system** with a strong emphasis on:

- **Correctness** through grounding and retrieval checks  
- **Explainability** via retrieved context and confidence scoring  
- **Modular, agent-based design** using LangGraph  

It showcases the practical application of **LangGraph** for building reliable, extensible, and interpretable AI pipelines.

---

## ⚠️ Notes

- `venv/` and `.env` are intentionally excluded from version control for security and portability
- Environment variables must be configured via:
  - `.env` file for local development
  - Platform-provided secrets for deployment environments

---

## 👤 Author

**Manoj PM**  
 B.E. student in Computer Science & Engineering  Graduate
Skilled in Full-Stack Development, AI/ML, and Agentic RAG Systems  

📧 *Open to AI Engineer / Software Development opportunities*

---


