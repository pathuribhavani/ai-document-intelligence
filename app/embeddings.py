from sklearn.feature_extraction.text import TfidfVectorizer


vectorizer = TfidfVectorizer()


def create_embeddings(chunks):
    embeddings = vectorizer.fit_transform(chunks)

    return embeddings