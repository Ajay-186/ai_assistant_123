import streamlit as st
import pandas as pd

from services.rag_service import database

from utils.vector_db import (
    database_information,
    get_database_statistics
)


# ==========================================================
# Vector Database Page
# ==========================================================

def show_vector_database():

    st.title("🗄 Vector Database")

    st.markdown(
        "View vectors stored inside ChromaDB."
    )

    st.divider()

    records = database()

    if records is None:

        st.warning("📂 Please upload a PDF first.")

        return

    # ======================================================
    # Database Information
    # ======================================================

    db = database_information()

    stats = get_database_statistics(records)

    c1, c2, c3 = st.columns(3)

    c1.metric(

        "Database",

        db["database"]

    )

    c2.metric(

        "Collections",

        len(db["collections"])

    )

    c3.metric(

        "Stored Vectors",

        stats["total_vectors"]

    )

    st.divider()

    # ======================================================
    # Database Details
    # ======================================================

    st.subheader("📂 Database Information")

    st.write(f"**Database :** {db['database']}")

    st.write(f"**Path :** {db['path']}")

    st.write(f"**Collection :** {stats['collection_name']}")

    st.divider()

    # ======================================================
    # Stored Records
    # ======================================================

    table = []

    for record in records:

        table.append({

            "Chunk ID": record["id"],

            "Dimension": record["embedding_dimension"],

            "Chunk Length": record["metadata"]["length"]

        })

    st.subheader("📊 Stored Records")

    st.dataframe(

        pd.DataFrame(table),

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # ======================================================
    # Individual Record
    # ======================================================

    selected = st.selectbox(

        "Select Chunk",

        [record["id"] for record in records]

    )

    selected_record = None

    for record in records:

        if record["id"] == selected:

            selected_record = record

            break

    if selected_record:

        st.subheader("📄 Chunk Information")

        st.write(f"**Chunk ID :** {selected_record['id']}")

        st.write(f"**Dimension :** {selected_record['embedding_dimension']}")

        st.write(f"**Chunk Number :** {selected_record['metadata']['chunk_number']}")

        st.write(f"**Start :** {selected_record['metadata']['start']}")

        st.write(f"**End :** {selected_record['metadata']['end']}")

        st.write(f"**Length :** {selected_record['metadata']['length']}")

        st.divider()

        st.subheader("📖 Stored Chunk")

        st.text_area(

            "",

            selected_record["document"],

            height=220,

            disabled=True

        )

        st.divider()

        st.subheader("🧠 Embedding Preview")

        st.json(

            selected_record["embedding_preview"]

        )

    st.divider()

    # ======================================================
    # Information
    # ======================================================

    st.info("""

### ChromaDB Storage

Each record contains:

• Chunk ID

• Chunk Text

• Embedding Vector

• Metadata

• Start Position

• End Position

• Chunk Length

These vectors are used during Semantic Search to retrieve the most relevant context before sending it to Gemini.

""")