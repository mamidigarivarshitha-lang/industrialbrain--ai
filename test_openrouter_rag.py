from modules.document_loader import load_documents
from modules.vector_store import (
    add_documents,
    search_documents
)

from modules.openrouter_helper import ask_llm

docs = load_documents("data/raw")

try:
    add_documents(docs)
except:
    pass

question = "Why did Pump P101 fail?"

results = search_documents(question)

context = "\n".join(
    results["documents"][0]
)

answer = ask_llm(
    question,
    context
)

print("\nANSWER:\n")
print(answer)