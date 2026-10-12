import os
import pickle
import numpy as np
import faiss

from config import (
    FAISS_INDEX_PATH,
    FAISS_METADATA_PATH,
    EMBEDDING_DIMENSION
)

# ==========================================================
# Create FAISS Index
# ==========================================================

def create_index():

    return faiss.IndexFlatL2(EMBEDDING_DIMENSION)


# ==========================================================
# Store Embeddings
# ==========================================================

def store_in_faiss(chunks, embeddings):

    os.makedirs("faiss_db", exist_ok=True)

    index = create_index()

    metadata = []

    vectors = []

    for chunk, embedding in zip(chunks, embeddings):

        vectors.append(embedding["vector"])

        metadata.append({

            "id": chunk["id"],

            "document": chunk["text"],

            "embedding_dimension": len(embedding["vector"]),

            "embedding_preview": embedding["vector"][:10],

            "metadata": {

                "chunk_id": chunk["id"],

                "chunk_number": chunk["chunk_number"],

                "start": chunk["start"],

                "end": chunk["end"],

                "length": chunk["length"]

            }

        })

    vectors = np.array(vectors).astype("float32")

    index.add(vectors)

    faiss.write_index(

        index,

        FAISS_INDEX_PATH

    )

    with open(

        FAISS_METADATA_PATH,

        "wb"

    ) as file:

        pickle.dump(metadata, file)

    return index


# ==========================================================
# Load FAISS Index
# ==========================================================

def load_index():

    if not os.path.exists(FAISS_INDEX_PATH):

        return None

    return faiss.read_index(

        FAISS_INDEX_PATH

    )


# ==========================================================
# Load Metadata
# ==========================================================

def load_metadata():

    if not os.path.exists(FAISS_METADATA_PATH):

        return []

    with open(

        FAISS_METADATA_PATH,

        "rb"

    ) as file:

        return pickle.load(file)


# ==========================================================
# Show Database
# ==========================================================

def show_database(index):

    return load_metadata()


# ==========================================================
# Database Statistics
# ==========================================================

def get_database_statistics(index):

    if index is None:

        return {

            "total_vectors": 0,

            "collection_name": "FAISS"

        }

    return {

        "total_vectors": index.ntotal,

        "collection_name": "FAISS Index"

    }


# ==========================================================
# Delete Database
# ==========================================================

def delete_collection():

    if os.path.exists(FAISS_INDEX_PATH):

        os.remove(FAISS_INDEX_PATH)

    if os.path.exists(FAISS_METADATA_PATH):

        os.remove(FAISS_METADATA_PATH)


# ==========================================================
# Database Information
# ==========================================================

def database_information():

    return {

        "database": "FAISS",

        "index_path": FAISS_INDEX_PATH,

        "metadata_path": FAISS_METADATA_PATH

    }