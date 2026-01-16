import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatIP(dim)
        self.texts = []
        self.metadata = []

    def add(self, vectors, texts, metadata):
        self.index.add(np.array(vectors))
        self.texts.extend(texts)
        self.metadata.extend(metadata)

    def search(self, vector, k: int):
        scores, indices = self.index.search(
            np.array([vector]), k
        )

        return [
            {
                "text": self.texts[i],
                "metadata": self.metadata[i]
            }
            for i in indices[0]
        ]
