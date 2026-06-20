import chromadb
from chromadb.utils import embedding_functions
import PyPDF2
from llm import ask_llm

embed_fn = embedding_functions.DefaultEmbeddingFunction()
chroma = chromadb.PersistentClient(path="./chroma_db")

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunks.append(" ".join(words[i : i + chunk_size]))
        i += chunk_size - overlap
    return chunks

def index_file(file):
    """Index uploaded file"""
    collection = chroma.get_or_create_collection("docs", embedding_function=embed_fn)
    
    text = "\n".join(page.extract_text() for page in PyPDF2.PdfReader(file).pages)
    chunks = chunk_text(text)
    
    texts, ids, metas = [], [], []
    for j, chunk in enumerate(chunks):
        texts.append(chunk)
        ids.append(f"{file.name}_{j}")
        metas.append({"source": file.name})
    
    collection.add(documents=texts, ids=ids, metadatas=metas)
    return len(chunks)

def query_documents(question: str) -> str:
    collection = chroma.get_collection("docs", embedding_function=embed_fn)
    chunks = collection.query(query_texts=[question], n_results=5)["documents"][0]
    context = "\n\n---\n\n".join(chunks)
    
    prompt = f"Answer using ONLY the context below.\n\nContext:\n{context}\n\nQuestion: {question}"
    return ask_llm(prompt)
