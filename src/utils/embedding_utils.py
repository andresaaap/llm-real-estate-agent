from typing import Union
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = 'all-MiniLM-L6-v2'  # Example model name

def generate_embeddings(input_data: Union[str, list[str]]) -> np.ndarray:
    model = SentenceTransformer(MODEL_NAME)
    embeddings = model.encode(input_data)
    return embeddings

def euclidean_distance(vec1, vec2):
    """
    Calculate the Euclidean distance between two vectors.
    """
    return np.linalg.norm(vec1 - vec2)

def find_nearest_neighbors(embedding, embeddings, k=5):
    """
    Find the k nearest neighbors for a given embedding.
    """
    distances = [euclidean_distance(embedding, e) for e in embeddings]
    nearest_neighbors = np.argsort(distances)[:k]
    return nearest_neighbors