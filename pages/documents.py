import streamlit as st

from utils.helper import (
    save_uploaded_file,
    delete_uploaded_file
)

from services.rag_service import (
    process_pdf,
    get_pdf_details
)


# ==========================================================
# Document Manager
# ==========================================================

def show_documents():

    st.title("📂 Document Manager")

    st.markdown(
        "Upload and manage your PDF documents."
    )

    st.divider()

    # ======================================================
    # Upload PDF
    # ======================================================

    uploaded_file = st.file_uploader(

        "Choose a PDF",

        type=["pdf"]

    )

    if uploaded_file is not None:

        if st.button("📤 Upload Document"):

            with st.spinner("Processing PDF..."):

                file_path = save_uploaded_file(
                    uploaded_file
                )

                process_pdf(file_path)

            st.success("Document uploaded successfully!")

            st.rerun()

    st.divider()

    # ======================================================
    # Current Document
    # ======================================================

    pdf = get_pdf_details()

    if pdf is None:

        st.info("No document uploaded.")

        return

    st.subheader("📄 Current Document")

    c1, c2 = st.columns(2)

    c1.metric(
        "Pages",
        pdf["pages"]
    )

    c2.metric(
        "Characters",
        pdf["characters"]
    )

    st.write(f"**File Name:** {pdf['file_name']}")

    st.write(f"**File Path:** {pdf['file_path']}")

    st.divider()

    # ======================================================
    # Preview
    # ======================================================

    st.subheader("📖 Preview")

    st.text_area(

        "",

        pdf["preview"],

        height=250,

        disabled=True

    )

    st.divider()

    # ======================================================
    # Metadata
    # ======================================================

    st.subheader("📋 Metadata")

    if pdf.get("metadata"):

        st.json(pdf["metadata"])

    else:

        st.info("No metadata available.")

    st.divider()

    # ======================================================
    # Delete
    # ======================================================

    if st.button("🗑 Delete Document"):

        delete_uploaded_file(
            pdf["file_path"]
        )

        st.success("Document deleted successfully!")

        st.rerun()