import streamlit as st

from config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    TOP_K,
    LLM_MODEL,
    EMBEDDING_MODEL,
    TEMPERATURE
)


# ==========================================================
# Settings Page
# ==========================================================

def show_settings():

    st.title("⚙ Settings")

    st.markdown(
        "Configure your GenAI Workspace."
    )

    st.divider()

    # ======================================================
    # RAG Settings
    # ======================================================

    st.subheader("📚 RAG Configuration")

    chunk_size = st.slider(

        "Chunk Size",

        min_value=100,

        max_value=1000,

        value=CHUNK_SIZE,

        step=50

    )

    chunk_overlap = st.slider(

        "Chunk Overlap",

        min_value=0,

        max_value=300,

        value=CHUNK_OVERLAP,

        step=10

    )

    top_k = st.slider(

        "Top K Retrieval",

        min_value=1,

        max_value=10,

        value=TOP_K

    )

    st.divider()

    # ======================================================
    # LLM Settings
    # ======================================================

    st.subheader("🤖 Gemini Configuration")

    model = st.selectbox(

        "LLM Model",

        [

            "gemini-2.5-flash",

            "gemini-2.5-pro"

        ],

        index=0

    )

    temperature = st.slider(

        "Temperature",

        min_value=0.0,

        max_value=1.0,

        value=float(TEMPERATURE),

        step=0.1

    )

    st.divider()

    # ======================================================
    # Embedding Settings
    # ======================================================

    st.subheader("🧠 Embedding Model")

    embedding = st.selectbox(

        "Embedding Model",

        [

            "all-MiniLM-L6-v2"

        ],

        index=0

    )

    st.divider()

    # ======================================================
    # Workspace Information
    # ======================================================

    st.subheader("ℹ Workspace Information")

    st.info(f"""

Application : GenAI Workspace

Architecture : Manual RAG

LLM : {LLM_MODEL}

Embedding Model : {EMBEDDING_MODEL}

Vector Database : ChromaDB

Python : 3.12+

Framework : Streamlit

""")

    st.divider()

    # ======================================================
    # Current Configuration
    # ======================================================

    st.subheader("📋 Current Configuration")

    st.json({

        "Chunk Size": chunk_size,

        "Chunk Overlap": chunk_overlap,

        "Top K": top_k,

        "LLM Model": model,

        "Embedding Model": embedding,

        "Temperature": temperature

    })

    st.divider()

    # ======================================================
    # Save Settings
    # ======================================================

    if st.button("💾 Save Settings", use_container_width=True):

        st.session_state["settings"] = {

            "chunk_size": chunk_size,

            "chunk_overlap": chunk_overlap,

            "top_k": top_k,

            "model": model,

            "embedding_model": embedding,

            "temperature": temperature

        }

        st.success("Settings Saved Successfully!")

    st.divider()

    # ======================================================
    # Reset Settings
    # ======================================================

    if st.button("🔄 Reset to Default", use_container_width=True):

        st.session_state.pop("settings", None)

        st.success("Settings Reset Successfully!")

        st.rerun()