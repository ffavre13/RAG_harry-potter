# RAG_harry-potter
Simple RAG (Retrieval-Augmented Generation) implementation for Harry Potter-themed question answering.

For the context, we use the harry potter movie scripts from Movie Script Database: [Movie Scripts](https://www.springfieldspringfield.co.uk).

For this project, we use ollama to generate embeddings and perform question answering. You'll need to download the 'embeddinggemma' model to run this project. You can do this by running the following commands in your terminal:
```bash
ollama pull embeddinggemma
```

For the question answering part, we use the 'gemma4:31b' model. You can get a free API key from [Ollama](https://ollama.com/) and set it in the `.env` file.

This project is inspired by the [RAG implementation video](https://www.youtube.com/watch?v=pvCabUerwss).

## Setup
1. Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/ffavre13/RAG_harry-potter.git && cd RAG_harry-potter
```
2. Install the required dependencies:
```bash
uv sync
```
3. Create a `.env` file in the project root and add your Ollama API key for the 'gemma4:31b' model.
```bash
echo "OLLAMA_API_KEY=<YOUR_OLLAMA_API_KEY>" > .env
```
4. Download the 'embeddinggemma' model by running:
```bash
ollama pull embeddinggemma
```
5. Run the main script to initialize the context and start asking questions:
```bash
uv run main.py
```

(optional) You can also run the Streamlit app to interact with the RAG system through a web interface:
```bash
uv run streamlit run app.py
```