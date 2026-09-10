# RAG_harry-potter
Simple RAG (Retrieval-Augmented Generation) implementation for Harry Potter-themed question answering.

For the context, we use the harry potter movie scripts from Movie Script Database: [Movie Scripts](https://www.springfieldspringfield.co.uk).

For this project, we use ollama to generate embeddings and perform question answering. You'll need to download the 'embeddinggemma' model to run this project. You can do this by running the following commands in your terminal:
```bash
ollama pull embeddinggemma
```

This project is strongly inspired by the [RAG implementation video](https://www.youtube.com/watch?v=pvCabUerwss).