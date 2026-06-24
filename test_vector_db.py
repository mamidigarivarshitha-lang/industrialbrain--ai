from modules.document_loader import load_documents
from modules.vector_store import (
    add_documents,
    search_documents
)

docs = load_documents("data/raw")

add_documents(docs)

results = search_documents(
    "Why did Pump P101 fail?"
)

print(results["documents"])