import streamlit as st
import plotly.express as px
import pandas as pd

from services.rag_service import (
    get_dashboard_stats,
    get_pdf_details
)


# ==========================================================
# Analytics Page
# ==========================================================

def show_analytics():

    st.title("📊 Analytics Dashboard")

    stats = get_dashboard_stats()

    pdf = get_pdf_details()

    if pdf is None:

        st.warning("Please upload a PDF first.")

        return

    # ------------------------------------------------------
    # Metrics
    # ------------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("📄 Pages", stats["pages"])
    c2.metric("🧩 Chunks", stats["chunks"])
    c3.metric("🧠 Embeddings", stats["vectors"])
    c4.metric("🔤 Characters", stats["characters"])

    st.divider()

    # ------------------------------------------------------
    # Document Information
    # ------------------------------------------------------

    st.subheader("📄 Document Information")

    document_df = pd.DataFrame({

        "Property": [

            "File Name",

            "Pages",

            "Characters"

        ],

        "Value": [

            pdf["file_name"],

            pdf["pages"],

            pdf["characters"]

        ]

    })

    st.dataframe(

        document_df,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # ------------------------------------------------------
    # Chunk Statistics
    # ------------------------------------------------------

    chunk_stats = stats["chunk_statistics"]

    chunk_df = pd.DataFrame({

        "Metric":[

            "Total Chunks",

            "Average Chunk Size",

            "Largest Chunk",

            "Smallest Chunk"

        ],

        "Value":[

            chunk_stats["total_chunks"],

            chunk_stats["average_chunk_size"],

            chunk_stats["largest_chunk"],

            chunk_stats["smallest_chunk"]

        ]

    })

    st.subheader("🧩 Chunk Statistics")

    st.dataframe(

        chunk_df,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # ------------------------------------------------------
    # Embedding Statistics
    # ------------------------------------------------------

    embedding_stats = stats["embedding_statistics"]

    embed_df = pd.DataFrame({

        "Metric":[

            "Embedding Dimension",

            "Total Embeddings"

        ],

        "Value":[

            embedding_stats["embedding_dimension"],

            embedding_stats["total_embeddings"]

        ]

    })

    st.subheader("🧠 Embedding Statistics")

    st.dataframe(

        embed_df,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # ------------------------------------------------------
    # Chart
    # ------------------------------------------------------

    chart_df = pd.DataFrame({

        "Category":[

            "Pages",

            "Chunks",

            "Embeddings"

        ],

        "Count":[

            stats["pages"],

            stats["chunks"],

            stats["vectors"]

        ]

    })

    fig = px.bar(

        chart_df,

        x="Category",

        y="Count",

        text="Count",

        title="GenAI Workspace Analytics"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    st.subheader("📖 Preview")

    st.text_area(

        "",

        pdf["preview"],

        height=250,

        disabled=True

    )