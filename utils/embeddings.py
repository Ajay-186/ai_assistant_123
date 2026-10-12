from sentence_transformers import SentenceTransformer

from config import EMBEDDING_MODEL


# ==========================================================
# Load Embedding Model
# ==========================================================

embedding_model = SentenceTransformer(
    EMBEDDING_MODEL
)


# ==========================================================
# Generate Embeddings
# ==========================================================

def generate_embeddings(chunks):

    embeddings = []

    for index, chunk in enumerate(chunks):

        vector = embedding_model.encode(
            chunk["text"]
        )

        embeddings.append({

            "embedding_id": f"embedding_{index+1}",

            "chunk_id": chunk["id"],

            "chunk_number": chunk["chunk_number"],

            "dimension": len(vector),

            "vector": vector.tolist()

        })

    return embeddings


# ==========================================================
# Embedding Statistics
# ==========================================================

def get_embedding_statistics(embeddings):

    if len(embeddings) == 0:

        return {

            "total_embeddings": 0,

            "embedding_dimension": 0

        }

    return {

        "total_embeddings": len(embeddings),

        "embedding_dimension": embeddings[0]["dimension"]

    }


# ==========================================================
# Embedding Preview
# ==========================================================

def get_embedding_preview(embeddings):

    preview = []

    for embedding in embeddings:

        preview.append({

            "Embedding ID": embedding["embedding_id"],

            "Chunk": embedding["chunk_number"],

            "Dimension": embedding["dimension"],

            "Preview": embedding["vector"][:10]

        })

    return preview


# ==========================================================
# Get Embedding By ID
# ==========================================================

def get_embedding_by_id(embeddings, embedding_id):

    for embedding in embeddings:

        if embedding["embedding_id"] == embedding_id:

            return embedding

    return None