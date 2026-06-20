# RAG Chatbot using Streamlit & Ollama

## Overview

This project is a Retrieval-Augmented Generation (RAG) chatbot built with **Streamlit** and **Ollama**. The chatbot retrieves relevant information from uploaded documents and generates context-aware responses using a local Large Language Model (LLM) served through Ollama.

## Features

* Upload and process documents (PDF, TXT, DOCX, etc.)
* Retrieval-Augmented Generation (RAG)
* Interactive chat interface with Streamlit
* Local LLM inference using Ollama
* Semantic search using vector embeddings
* Fast and privacy-friendly document querying

## Tech Stack

* **Frontend:** Streamlit
* **LLM:** Ollama
* **Embeddings:** Ollama Embeddings / Sentence Transformers
* **Vector Database:** ChromaDB / FAISS
* **Language:** Python

## Project Structure

```bash
rag-chatbot/
│
├── app.py
├── requirements.txt
├── data/
│   └── documents
├── vectorstore/
├── utils/
│   ├── document_loader.py
│   ├── embeddings.py
│   └── retriever.py
├── assets/
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Install Ollama

Download and install Ollama from:

https://ollama.com

Pull a model:

```bash
ollama pull llama3
```

Verify installation:

```bash
ollama run llama3
```

## Run the Application

Start Ollama:

```bash
ollama serve
```

Run Streamlit:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

## How It Works

1. User uploads documents.
2. Documents are split into chunks.
3. Embeddings are generated and stored in a vector database.
4. Relevant chunks are retrieved based on user queries.
5. Retrieved context is sent to the Ollama model.
6. The model generates accurate responses using the retrieved information.

## Example Query

```text
User: What are the key features mentioned in the document?

Bot: Based on the uploaded document, the key features include...
```

## Requirements

```text
streamlit
langchain
langchain-community
chromadb
faiss-cpu
pypdf
sentence-transformers
ollama
python-dotenv
```

## Future Enhancements

* Chat history memory
* Multiple document support
* Conversation summarization
* Authentication system
* Deployment on cloud platforms

## Author

Ganesh Paidi

## License

This project is licensed under the MIT License.
