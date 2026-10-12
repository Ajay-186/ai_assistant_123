import streamlit as st

from services.rag_service import (
    generate_notes,
    get_pdf_details
)


# ==========================================================
# AI Notes Page
# ==========================================================

def show_notes():

    st.title("📝 AI Study Notes")

    st.markdown(
        "Generate structured study notes from the uploaded document."
    )

    st.divider()

    # ======================================================
    # Check Document
    # ======================================================

    pdf = get_pdf_details()

    if pdf is None:

        st.warning("📂 Please upload a PDF first.")

        return

    st.success(f"Current Document : {pdf['file_name']}")

    st.divider()

    # ======================================================
    # Generate Notes
    # ======================================================

    if st.button("📝 Generate Notes"):

        with st.spinner("Generating Study Notes..."):

            notes = generate_notes()

            st.session_state["notes"] = notes

    # ======================================================
    # Display Notes
    # ======================================================

    if "notes" in st.session_state:

        st.subheader("📚 Generated Notes")

        st.markdown(st.session_state["notes"])

        st.download_button(

            label="⬇ Download Notes",

            data=st.session_state["notes"],

            file_name="study_notes.txt",

            mime="text/plain"

        )

    st.divider()

    # ======================================================
    # Information
    # ======================================================

    st.info("""

### AI Study Notes

The generated notes include:

✅ Important Topics

✅ Key Concepts

✅ Definitions

✅ Bullet Points

✅ Revision Notes

These notes are generated directly from the uploaded document using the RAG pipeline.

""")