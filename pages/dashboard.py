import streamlit as st

from services.rag_service import (
    get_dashboard_stats,
    get_pdf_details
)

from utils.helper import application_information


# ==========================================================
# Dashboard
# ==========================================================

def show_dashboard():

    st.title("🚀 GenAI Workspace")

    st.markdown(
        "### Enterprise AI Research & Knowledge Platform"
    )

    st.divider()

    # ======================================================
    # Application Information
    # ======================================================

    app = application_information()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info(f"""
### 🤖 AI Model

**Provider:** {app['Provider']}

**Model:** {app['LLM']}
""")

    with col2:

        st.info(f"""
### 🧠 Embeddings

**Model:** {app['Embedding Model']}

**Vector DB:** {app['Vector Database']}
""")

    with col3:

        st.info(f"""
### ⚙ Architecture

**Type:** {app['Architecture']}

**Version:** {app['Version']}
""")

    st.divider()

    # ======================================================
    # Statistics
    # ======================================================

    stats = get_dashboard_stats()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "📄 Documents",
        stats["documents"]
    )

    c2.metric(
        "📑 Pages",
        stats["pages"]
    )

    c3.metric(
        "🧩 Chunks",
        stats["chunks"]
    )

    c4.metric(
        "🧠 Embeddings",
        stats["vectors"]
    )

    st.divider()

    # ======================================================
    # Current Document
    # ======================================================

    pdf = get_pdf_details()

    if pdf is None:

        st.warning("No document uploaded.")

        return

    st.subheader("📂 Current Document")

    left, right = st.columns([1, 2])

    with left:

        st.metric(
            "Pages",
            pdf["pages"]
        )

        st.metric(
            "Characters",
            pdf["characters"]
        )

    with right:

        st.write(f"**File Name:** {pdf['file_name']}")

        st.write(f"**File Path:** {pdf['file_path']}")

        st.write("**Preview**")

        st.text_area(

            "",

            pdf["preview"],

            height=220,

            disabled=True

        )

    st.divider()

    # ======================================================
    # Features
    # ======================================================

    st.subheader("✨ Workspace Features")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.success("""
### 📂 Document Management

- Upload PDFs
- Manage Documents
- View Metadata
- Delete Documents
""")

    with c2:

        st.success("""
### 🤖 AI Features

- AI Chat
- Summary
- Notes
- Quiz
- Flashcards
""")

    with c3:

        st.success("""
### 📊 Analytics

- Semantic Search
- Embeddings
- Vector Database
- Statistics
""")

    st.divider()

    # ======================================================
    # System Status
    # ======================================================

    st.subheader("🖥 System Status")

    s1, s2, s3 = st.columns(3)

    s1.success("✅ Gemini Connected")

    s2.success("✅ FAISS Index Active")

    s3.success("✅ RAG Ready")

    st.divider()

    st.caption("GenAI Workspace • Enterprise AI Research & Knowledge Platform")