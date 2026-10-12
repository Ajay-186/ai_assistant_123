import numpy as np
from sentence_transformers import SentenceTransformer

from config import EMBEDDING_MODEL
from config import TOP_K

from utils.vector_db import load_metadata


# ==========================================================
# Load Embedding Model
# ==========================================================

embedding_model = SentenceTransformer(
    EMBEDDING_MODEL
)


# ==========================================================
# Semantic Search
# ==========================================================

def semantic_search(index, question, top_k=TOP_K):

    metadata = load_metadata()

    query_vector = embedding_model.encode(
        question
    )

    query_vector = np.array(
        [query_vector]
    ).astype("float32")

    distances, indices = index.search(
        query_vector,
        top_k
    )

    results = []

    for rank, idx in enumerate(indices[0]):

        if idx == -1:
            continue

        item = metadata[idx]

        similarity = float(
            1 / (1 + distances[0][rank])
        )

        results.append({

            "rank": rank + 1,

            "chunk_id": item["metadata"]["chunk_id"],

            "chunk_number": item["metadata"]["chunk_number"],

            "document": item["document"],

            "similarity": round(similarity, 4),

            "metadata": item["metadata"]

        })

    return results


# ==========================================================
# Best Match
# ==========================================================

def get_best_match(results):

    if len(results) == 0:

        return None

    return results[0]


# ==========================================================
# Search Statistics
# ==========================================================

def get_search_statistics(results):

    if len(results) == 0:

        return {

            "results_found": 0,

            "highest_similarity": 0,

            "average_similarity": 0

        }

    similarities = [

        item["similarity"]

        for item in results

    ]

    return {

        "results_found": len(results),

        "highest_similarity": max(similarities),

        "average_similarity": round(

            sum(similarities) / len(similarities),

            4

        )

    }


# ==========================================================
# Build Context
# ==========================================================

def build_context(results):

    context = ""

    for item in results:

        context += item["document"]

        context += "\n\n"

    return context.strip()