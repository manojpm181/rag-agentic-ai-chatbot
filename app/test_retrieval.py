from retriever import get_retriever

if __name__ == "__main__":
    retriever = get_retriever(top_k=4)

    query = "What is Agentic AI?"
    docs = retriever.invoke(query)

    print(f"\n🔍 Query: {query}\n")
    for i, doc in enumerate(docs):
        print(f"--- Chunk {i+1} ---")
        print(doc.page_content[:500])
        print("\n")
