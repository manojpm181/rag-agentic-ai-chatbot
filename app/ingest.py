from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter

PDF_PATH = "data/agentic_ai_ebook.pdf"
DB_DIR = "vectorstore"

loader = PyPDFLoader(PDF_PATH)
pages = loader.load()

print(f"Loaded {len(pages)} pages")

# 🔴 HARD CHECK — THIS MUST LOOK LIKE PDF TEXT
print("\nSAMPLE RAW PAGE:\n")
print(pages[0].page_content[:800])

splitter = RecursiveCharacterTextSplitter(
    chunk_size=600,
    chunk_overlap=150
)

docs = splitter.split_documents(pages)

print(f"\nCreated {len(docs)} chunks")

print("\nSAMPLE CHUNK:\n")
print(docs[5].page_content[:800])

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory=DB_DIR
)

print("✅ Vectorstore rebuilt from PDF ONLY")

