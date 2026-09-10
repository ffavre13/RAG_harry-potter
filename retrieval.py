import ollama

def search(question, collection, n_results=3):
    """
    Search for relevant chunks in the ChromaDB collection based on the question.
    """
    response = ollama.embed(
        model='embeddinggemma',
        input=[question]
    )
    question_embedding = response['embeddings'][0]
    
    print(f"Searching for relevant chunks for the question: '{question}'...")
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=n_results
    )
    
    return results