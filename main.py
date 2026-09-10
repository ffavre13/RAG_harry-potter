from dataIngestion import load_scripts, clean_script, split_script_into_chunks
from embeddings import generate_embeddings, save_embeddings_to_chromadb, is_embeddings_saved
from retrieval import search
import nltk
import chromadb

def initialize_context():
    """
    Initialize the context by loading and processing the Harry Potter movie scripts.
    """
    harry_potter_scripts = [
        {
            "title": "Harry Potter and the Philosopher's Stone",
            "url": "https://www.springfieldspringfield.co.uk/movie_script.php?movie=harry-potter-and-the-sorcerers-stone"  
        },
        {
            "title": "Harry Potter and the Chamber of Secrets",
            "url": "https://www.springfieldspringfield.co.uk/movie_script.php?movie=harry-potter-and-the-chamber-of-secrets"
        },
        {
            "title": "Harry Potter and the Prisoner of Azkaban",
            "url": "https://www.springfieldspringfield.co.uk/movie_script.php?movie=harry-potter-and-the-prisoner-of-azkaban"
        }
    ]
    nltk.download('punkt')
    all_chunks = []
    
    print("Loading Harry Potter movie scripts...")    
    # Load and process each script
    for script in harry_potter_scripts:
        print(f"Loading script for {script['title']}...")
        script_content = load_scripts(script['url'])
        script_content = clean_script(script_content)
        chunks = split_script_into_chunks(script_content, script['title'])
        all_chunks.extend(chunks)
        
    return all_chunks

def main():
    # ChromaDB client setup
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(name="harry_potter_scripts")
    
    # Check if embeddings are already saved in the ChromaDB collection
    if is_embeddings_saved(collection):
        print("Embeddings are already saved in ChromaDB. Skipping embedding generation.")
    else:
        print("Embeddings not found in ChromaDB. Generating embeddings...")
        chunks = initialize_context()
        embeddings = generate_embeddings(chunks)
        save_embeddings_to_chromadb(embeddings, collection)

    

if __name__ == "__main__":
    main()