from config import CHUNK_SIZE, CHUNK_OVERLAP


# ==========================================================
# Create Chunks
# ==========================================================

def create_chunks(
    text,
    chunk_size=CHUNK_SIZE,
    overlap=CHUNK_OVERLAP
):

    chunks = []

    start = 0

    chunk_number = 1

    while start < len(text):

        end = min(start + chunk_size, len(text))

        chunk_text = text[start:end]

        chunk = {

            "id": f"chunk_{chunk_number}",

            "chunk_number": chunk_number,

            "text": chunk_text,

            "start": start,

            "end": end,

            "length": len(chunk_text),

            "preview": chunk_text[:120]

        }

        chunks.append(chunk)

        chunk_number += 1

        start += chunk_size - overlap

    return chunks


# ==========================================================
# Chunk Statistics
# ==========================================================

def get_chunk_statistics(chunks):

    if len(chunks) == 0:

        return {

            "total_chunks": 0,

            "average_chunk_size": 0,

            "largest_chunk": 0,

            "smallest_chunk": 0,

            "total_characters": 0

        }

    sizes = [chunk["length"] for chunk in chunks]

    return {

        "total_chunks": len(chunks),

        "average_chunk_size": round(sum(sizes) / len(sizes), 2),

        "largest_chunk": max(sizes),

        "smallest_chunk": min(sizes),

        "total_characters": sum(sizes)

    }


# ==========================================================
# Get Chunk By ID
# ==========================================================

def get_chunk_by_id(chunks, chunk_id):

    for chunk in chunks:

        if chunk["id"] == chunk_id:

            return chunk

    return None


# ==========================================================
# Get Chunk Preview
# ==========================================================

def get_chunk_preview(chunks):

    preview = []

    for chunk in chunks:

        preview.append({

            "Chunk ID": chunk["id"],

            "Chunk Number": chunk["chunk_number"],

            "Length": chunk["length"],

            "Preview": chunk["preview"]

        })

    return preview