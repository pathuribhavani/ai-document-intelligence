import chromadb
from sentence_transformers import SentenceTransformer


class DocumentSearch:

    def __init__(self, chunks):

        self.chunks = chunks

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

        embeddings = self.model.encode(
            chunks
        ).tolist()

        ids = [
            f"chunk_{i}"
            for i in range(len(chunks))
        ]

        self.collection.upsert(
            ids=ids,
            documents=chunks,
            embeddings=embeddings
        )

    def search(self, query, top_k=3):

        query_embedding = self.model.encode(
            [query]
        ).tolist()

        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=top_k
        )

        chunks = results["documents"][0]
        distances = results["distances"][0]

        search_results = []

        for chunk, distance in zip(chunks, distances):

            score = 1 - distance

            search_results.append({
                "chunk": chunk,
                "score": float(score)
            })

        return search_results