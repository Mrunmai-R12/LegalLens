from sentence_transformers import SentenceTransformer

# Legal-domain embedding model
_model = SentenceTransformer("nlpaueb/legal-bert-base-uncased")

def embed(texts):
    """
    Convert text chunks or queries into dense vectors
    using Legal-BERT for semantic retrieval.
    """
    return _model.encode(texts, normalize_embeddings=True)
