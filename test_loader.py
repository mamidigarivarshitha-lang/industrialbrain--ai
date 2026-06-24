from modules.document_loader import load_documents

docs = load_documents("data/raw")

for doc in docs:
    print("\n----------------")
    print(doc["file_name"])
    print(doc["content"])