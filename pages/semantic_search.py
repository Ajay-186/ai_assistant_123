import streamlit as st
import pandas as pd

from services.rag_service import (
    search,
    get_pdf_details
)

from utils.retriever import (
    get_search_statistics
)


# ==========================================================
# Semantic Search Page
# ==========================================================

def show_semantic_search():

    st.title("🔍 Semantic Search")

    st.markdown(
        "Search semantically through the uploaded document using FAISS and Sentence Transformers."
    )

    st.divider()

    # ======================================================
    # Check Uploaded PDF
    # ======================================================

    pdf = get_pdf_details()

    if pdf is None:

        st.warning("📂 Please upload a PDF first.")

        return

    st.success(f"Current Document : {pdf['file_name']}")

    st.divider()

    # ======================================================
    # Search Query
    # ======================================================

    query = st.text_input(

        "Enter your question or search query"

    )

    if st.button("🔍 Search"):

        if query.strip() == "":

            st.warning("Please enter a search query.")

            return

        with st.spinner("Searching FAISS Index..."):

            results = search(query)

            st.session_state["search_results"] = results

    # ======================================================
    # Display Results
    # ======================================================

    if "search_results" not in st.session_state:

        return

    results = st.session_state["search_results"]

    if len(results) == 0:

        st.error("No matching chunks found.")

        return

    st.divider()

    # ======================================================
    # Statistics
    # ======================================================

    stats = get_search_statistics(results)

    c1, c2, c3 = st.columns(3)

    c1.metric(

        "Results Found",

        stats["results_found"]

    )

    c2.metric(

        "Highest Similarity",

        f"{stats['highest_similarity']:.2%}"

    )

    c3.metric(

        "Average Similarity",

        f"{stats['average_similarity']:.2%}"

    )

    st.divider()

    # ======================================================
    # Results Table
    # ======================================================

    st.subheader("📊 Search Results")

    table = []

    for item in results:

        table.append({

            "Rank": item["rank"],

            "Chunk": item["chunk_number"],

            "Similarity": f"{item['similarity']:.2%}"

        })

    st.dataframe(

        pd.DataFrame(table),

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # ======================================================
    # Retrieved Chunks
    # ======================================================

    st.subheader("📄 Retrieved Chunks")

    for item in results:

        with st.expander(

            f"Rank {item['rank']} | Similarity : {item['similarity']:.2%}"

        ):

            st.write(f"**Chunk ID :** {item['chunk_id']}")

            st.write(f"**Chunk Number :** {item['chunk_number']}")

            st.write(f"**Similarity Score :** {item['similarity']:.4f}")

            st.write("### Retrieved Text")

            st.write(item["document"])

    st.divider()

    # ======================================================
    # Workflow
    # ======================================================

    st.subheader("⚙ Manual RAG Workflow")

    st.info("""

### How Semantic Search Works

1️⃣ User enters a query.

2️⃣ The query is converted into an embedding using **Sentence Transformers**.

3️⃣ The embedding is searched against the **FAISS Vector Index**.

4️⃣ FAISS retrieves the **Top-K most similar chunks**.

5️⃣ The retrieved chunks are combined into a context.

6️⃣ The context is sent to **Google Gemini**.

7️⃣ Gemini generates the final answer.

""")

    st.divider()

    # ======================================================
    # About Similarity
    # ======================================================

    st.subheader("📘 About Similarity Score")

    st.write("""

- **100%** → Almost identical meaning.

- **80% - 99%** → Highly relevant.

- **60% - 79%** → Moderately relevant.

- **Below 60%** → Weak semantic similarity.

The similarity score is calculated from the vector distance returned by the FAISS index.

""")