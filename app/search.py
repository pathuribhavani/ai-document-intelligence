from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class DocumentSearch:

    def __init__(self, chunks):
        self.chunks = chunks

        self.vectorizer = TfidfVectorizer()

        self.chunk_vectors = self.vectorizer.fit_transform(chunks)

    def search(self, query, top_k=3):

        query_vector = self.vectorizer.transform([query])

        similarities = cosine_similarity(
            query_vector,
            self.chunk_vectors
        )[0]

        top_indices = similarities.argsort()[::-1][:top_k]

        results = []

        for index in top_indices:
            results.append({
                "chunk": self.chunks[index],
                "score": float(similarities[index])
            })

        return results