import os
from ollama import Client

def generate_response(question, results):
    """
    Generate a response based on the question and the retrieved results.
    """
    documents = results['documents'][0]
    metadatas = results['metadatas'][0]
    context = ""
    
    for meta, doc in zip(metadatas, documents):
        context += f"Title: {meta['title']}\nExcerpt: {doc}\n\n"
        
    prompt = f"""
    You are a Harry Potter expert. Use ONLY the following script excerpts to answer the question.
    If the answer is not contained within the excerpts, say "There is no information about this in the harry potter script."
    
    Context:
    {context}
    
    Question: {question}
    
    Answer:
    """
    
    client = Client(
        host="https://ollama.com",
        headers={"Authorization": "Bearer " + os.getenv("OLLAMA_API_KEY")}
    )
    
    response = client.chat(
        model="gemma4:31b",
        messages=[{"role": "user", "content": prompt}],
    )
    
    answer = response["message"]["content"]
    
    return answer