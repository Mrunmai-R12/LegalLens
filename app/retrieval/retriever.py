from app.startup import get_vector_store
from app.retrieval.embeddings import embed
from app.config import settings

def retrieve(query: str):
    store = get_vector_store()
    query_vector = embed([query])[0]
    return store.search(query_vector, settings.TOP_K)
