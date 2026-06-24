from modules.document_loader import load_documents
from modules.vector_store import add_documents
from modules.vector_store import search_documents

from modules.openrouter_helper import ask_llm


def ask_question(question):

    docs = load_documents("data/raw")

    try:
        add_documents(docs)
    except:
        pass

    results = search_documents(question)

    context = "\n".join(
        results["documents"][0]
    )

    answer = ask_llm(
        question,
        context
    )

    return answer