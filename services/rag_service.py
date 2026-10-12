import os

from utils.pdf_reader import read_pdf
from utils.chunking import (
    create_chunks,
    get_chunk_statistics
)

from utils.embeddings import (
    generate_embeddings,
    get_embedding_statistics
)

from utils.vector_db import (
    store_in_faiss,
    show_database
)

from utils.retriever import semantic_search

from utils.prompt_builder import build_prompt

from utils.gemini_llm import generate_answer


# ==========================================================
# Global Variables
# ==========================================================

index = None

pdf_details = None

chunk_objects = None

embedding_objects = None


# ==========================================================
# Process PDF
# ==========================================================

def process_pdf(pdf_path):

    global index
    global pdf_details
    global chunk_objects
    global embedding_objects

    if not os.path.exists(pdf_path):

        raise FileNotFoundError("PDF Not Found.")

    # Read PDF

    pdf = read_pdf(pdf_path)

    pdf_details = pdf

    # Chunking

    chunk_objects = create_chunks(

        pdf["text"]

    )

    # Embeddings

    embedding_objects = generate_embeddings(

        chunk_objects

    )

    # Store in FAISS

    index = store_in_faiss(

        chunk_objects,

        embedding_objects

    )

    return {

        "pdf": pdf_details,

        "chunks": chunk_objects,

        "embeddings": embedding_objects,

        "index": index

    }


# ==========================================================
# Chat
# ==========================================================

def chat(question):

    global index

    if index is None:

        return "Please upload a PDF first."

    retrieved_chunks = semantic_search(

        index,

        question

    )

    prompt = build_prompt(

        question,

        retrieved_chunks

    )

    result = generate_answer(prompt)

    return result["response"]


# ==========================================================
# Summary
# ==========================================================

def summarize(summary_type="Detailed Summary"):

    question = f"""

Generate a {summary_type}.

Include:

• Main Topics

• Key Concepts

• Important Points

• Conclusion

"""

    return chat(question)


# ==========================================================
# Notes
# ==========================================================

def generate_notes():

    question = """

Generate detailed study notes.

Include:

1. Headings

2. Important Concepts

3. Definitions

4. Revision Notes

"""

    return chat(question)


# ==========================================================
# Quiz
# ==========================================================

def generate_quiz(

    difficulty="Medium",

    total_questions=10

):

    question = f"""

Generate {total_questions} MCQs.

Difficulty : {difficulty}

Provide:

Question

4 Options

Correct Answer

"""

    return chat(question)


# ==========================================================
# Flashcards
# ==========================================================

def generate_flashcards():

    return chat(

        "Generate Question and Answer flashcards."

    )


# ==========================================================
# Interview Questions
# ==========================================================

def generate_interview_questions():

    return chat(

        """
Generate Beginner,
Intermediate,
Advanced interview questions
with answers.
"""

    )


# ==========================================================
# Semantic Search
# ==========================================================

def search(query):

    global index

    if index is None:

        return []

    return semantic_search(

        index,

        query

    )


# ==========================================================
# Database
# ==========================================================

def database():

    global index

    if index is None:

        return None, None

    records = show_database(

        index

    )

    return records, index


# ==========================================================
# PDF Details
# ==========================================================

def get_pdf_details():

    return pdf_details


# ==========================================================
# Chunks
# ==========================================================

def get_chunks():

    return chunk_objects


# ==========================================================
# Embeddings
# ==========================================================

def get_embeddings():

    return embedding_objects


# ==========================================================
# Dashboard Statistics
# ==========================================================

def get_dashboard_stats():

    global index

    if index is None:

        return {

            "documents": 0,

            "pages": 0,

            "characters": 0,

            "chunks": 0,

            "vectors": 0,

            "chunk_objects": [],

            "embedding_objects": []

        }

    return {

        "documents": 1,

        "pages": pdf_details["pages"],

        "characters": pdf_details["characters"],

        "chunks": len(chunk_objects),

        "vectors": index.ntotal,

        "chunk_objects": chunk_objects,

        "embedding_objects": embedding_objects,

        "chunk_statistics": get_chunk_statistics(chunk_objects),

        "embedding_statistics": get_embedding_statistics(embedding_objects)

    }