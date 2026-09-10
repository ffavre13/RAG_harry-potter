import ollama

def generate_embeddings(chunks):
    """
    Generate embeddings for a list of text chunks.
    https://docs.ollama.com/capabilities/embeddings#python
    """
    embeddings = []
    
    print("Generating embeddings for the chunks...")    
    batch = ollama.embed(
        model='embeddinggemma',
        input=[chunk['text'] for chunk in chunks]
    )
    print("Embeddings generated successfully.")
    
    for i, chunk in enumerate(chunks):
        embeddings.append({
            "title": chunk['title'],
            "text": chunk['text'],
            "embedding": batch['embeddings'][i]
        })
    
    return embeddings

def save_embeddings_to_chromadb(embeddings, collection):
    """
    Save the generated embeddings to a ChromaDB collection.
    """
    
    print("Saving embeddings to ChromaDB...")
    collection.add(
        ids=[f"chunk_{i}" for i in range(len(embeddings))],
        documents=[embedding['text'] for embedding in embeddings],
        metadatas=[{"title": embedding['title']} for embedding in embeddings],
        embeddings=[embedding['embedding'] for embedding in embeddings]
    )
    print("Embeddings saved to ChromaDB successfully.")
    
def is_embeddings_saved(collection):
    """
    Check if embeddings are already saved in the ChromaDB collection.
    """
    
    return collection.count() > 0