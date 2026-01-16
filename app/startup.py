from app.ingestion.chunker import clause_chunk
from app.retrieval.embeddings import embed
from app.retrieval.vector_store import VectorStore

_vector_store = None

def load_documents():
    global _vector_store

    with open("data/sample_contract.txt", "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()


    chunks = clause_chunk(text)
    texts = [c["text"] for c in chunks]
    metadata = [c["metadata"] for c in chunks]

    embeddings = embed(texts)

    store = VectorStore(dim=len(embeddings[0]))
    store.add(embeddings, texts, metadata)

    _vector_store = store

def get_vector_store():
    if _vector_store is None:
        raise RuntimeError("Vector store not initialized")
    return _vector_store
