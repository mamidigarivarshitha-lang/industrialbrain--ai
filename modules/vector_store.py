import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="vector_db")

collection = client.get_or_create_collection(
    name="industrial_documents"
)


def add_documents(documents):

    for idx, doc in enumerate(documents):

        embedding = model.encode(doc["content"]).tolist()

        collection.add(
            ids=[str(idx)],
            embeddings=[embedding],
            documents=[doc["content"]],
            metadatas=[
                {
                    "file_name": doc["file_name"]
                }
            ]
        )


def search_documents(query):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )

    return results