import streamlit as st
import pandas as pd

from services.rag_service import (
    get_dashboard_stats,
    get_pdf_details
)

from utils.embeddings import (
    get_embedding_statistics,
    get_embedding_preview
)


# ==========================================================
# Embeddings Viewer
# ==========================================================

def show_embeddings():

    st.title("🧠 Embeddings Viewer")

    st.markdown(
        "Explore the vector embeddings generated for each document chunk."
    )

    st.divider()

    pdf = get_pdf_details()

    if pdf is None:

        st.warning("📂 Please upload a PDF first.")

        return

    stats = get_dashboard_stats()

    embeddings = stats["embedding_objects"]

    if len(embeddings) == 0:

        st.warning("No embeddings available.")

        return

    # ======================================================
    # Statistics
    # ======================================================

    embedding_stats = get_embedding_statistics(
        embeddings
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(

        "Total Embeddings",

        embedding_stats["total_embeddings"]

    )

    c2.metric(

        "Embedding Dimension",

        embedding_stats["embedding_dimension"]

    )

    c3.metric(

        "Embedding Model",

        "all-MiniLM-L6-v2"

    )

    st.divider()

    # ======================================================
    # Embedding Table
    # ======================================================

    st.subheader("📊 Embedding Information")

    preview = get_embedding_preview(
        embeddings
    )

    st.dataframe(

        pd.DataFrame(preview),

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # ======================================================
    # Inspect Embedding
    # ======================================================

    st.subheader("🔍 Inspect Embedding")

    embedding_ids = [

        item["Embedding ID"]

        for item in preview

    ]

    selected = st.selectbox(

        "Select Embedding",

        embedding_ids

    )

    selected_embedding = None

    for embedding in embeddings:

        if embedding["embedding_id"] == selected:

            selected_embedding = embedding

            break

    if selected_embedding:

        st.write("### Chunk ID")

        st.code(selected_embedding["chunk_id"])

        st.write("### Chunk Number")

        st.code(selected_embedding["chunk_number"])

        st.write("### Vector Dimension")

        st.code(selected_embedding["dimension"])

        st.write("### First 20 Values")

        st.json(

            selected_embedding["vector"][:20]

        )

        st.write("### Complete Vector")

        st.text_area(

            "Embedding Vector",

            str(selected_embedding["vector"]),

            height=300,

            disabled=True

        )

    st.divider()

    # ======================================================
    # About Embeddings
    # ======================================================

    st.subheader("📘 What are Embeddings?")

    st.info("""

Embeddings are numerical vector representations of text.

### Workflow

1️⃣ PDF is divided into chunks.

2️⃣ Each chunk is converted into a **384-dimensional vector** using Sentence Transformers.

3️⃣ The vectors are stored inside the **FAISS Vector Index**.

4️⃣ During semantic search, the user's question is also converted into an embedding.

5️⃣ FAISS compares the query embedding with all stored embeddings.

6️⃣ The most similar chunks are retrieved and sent to Google Gemini.

Embeddings are the foundation of Retrieval-Augmented Generation (RAG).

""")