from modules.document_loader import load_documents
from modules.vector_store import add_documents, search_documents
from modules.openrouter_helper import ask_llm


def ask_question(question):

    # Load all documents
    docs = load_documents("data/raw")
    
    print("\nLOADED DOCUMENTS:")
    print(docs)

    # Add documents to vector database
    add_documents(docs)

    # Search relevant documents
    results = search_documents(question)

    print("\n====================")
    print("SEARCH RESULTS:")
    print(results)
    print("====================")

    # Extract retrieved context
    context = ""

    if len(results["documents"]) > 0:
        context = "\n\n".join(results["documents"][0])

    print("\n====================")
    print("CONTEXT SENT TO LLM:")
    print(context)
    print("====================")

    # Ask LLM using retrieved context
    answer = ask_llm(
        question=question,
        context=context
    )

    return answer