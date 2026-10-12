import streamlit as st

from services.rag_service import (
    generate_flashcards,
    get_pdf_details
)


# ==========================================================
# Flashcards Page
# ==========================================================

def show_flashcards():

    st.title("🃏 AI Flashcards")

    st.markdown(
        "Generate AI-powered flashcards from the uploaded document."
    )

    st.divider()

    pdf = get_pdf_details()

    if pdf is None:

        st.warning("📂 Please upload a PDF first.")

        return

    st.success(f"Current Document : {pdf['file_name']}")

    st.divider()

    # ======================================================
    # Generate Flashcards
    # ======================================================

    if st.button("🚀 Generate Flashcards"):

        with st.spinner("Generating Flashcards..."):

            flashcards = generate_flashcards()

            st.session_state["flashcards"] = flashcards

    # ======================================================
    # Display Flashcards
    # ======================================================

    if "flashcards" in st.session_state:

        st.subheader("🃏 Generated Flashcards")

        st.markdown(st.session_state["flashcards"])

        st.download_button(

            label="⬇ Download Flashcards",

            data=st.session_state["flashcards"],

            file_name="flashcards.txt",

            mime="text/plain"

        )

    st.divider()

    # ======================================================
    # Information
    # ======================================================

    st.info("""

### Flashcards are useful for:

- 📚 Revision

- 🎯 Exam Preparation

- 💼 Interview Preparation

- 🧠 Quick Learning

The AI automatically creates Question & Answer style flashcards from your uploaded document.

""")