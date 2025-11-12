import os
import numpy as np
import openai
from dotenv import load_dotenv
from utils import extract_text_from_pdf, split_text, create_embeddings
from prompt import OpenAIConfig
from vectordb import VectorStore

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
ai = OpenAIConfig(api_key=api_key)

vector_store = VectorStore(dim=1536)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def process_pdf(file):
    text = extract_text_from_pdf(file)
    chunks = split_text(text)
    embeddings = create_embeddings(chunks)

    texts = [chunk["text"] for chunk in embeddings]
    vectors = [chunk["embedding"] for chunk in embeddings]

    print("Embedding dimension:", len(vectors[0]))

    vector_store.add(vectors, texts)
    return embeddings

def query_pdf(user_input, history):
    response = openai.embeddings.create(
        model="text-embedding-3-small",
        input=user_input
    )

    user_embedding = response.data[0].embedding

    print("User Embedding dimension:", len(user_embedding))
    
    top_chunks = vector_store.search(user_embedding, top_k=3)
    relevant_text = "\n\n".join(top_chunks)

    prompt = f"""Based on this context:\n{relevant_text}\n\nAnswer the question:\n{user_input}. Guide user when necessary."""
    response = ai.get_response(prompt, history)
    return response
