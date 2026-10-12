import streamlit as st

from services.rag_service import (
    generate_interview_questions,
    get_pdf_details
)


# ==========================================================
# Interview Questions Page
# ==========================================================

def show_interview():

    st.title("💼 AI Interview Questions")

    st.markdown(
        "Generate interview questions from the uploaded document."
    )

    st.divider()

    pdf = get_pdf_details()

    if pdf is None:

        st.warning("📂 Please upload a PDF first.")

        return

    st.success(f"Current Document : {pdf['file_name']}")

    st.divider()

    # ======================================================
    # Generate Interview Questions
    # ======================================================

    if st.button("🚀 Generate Interview Questions"):

        with st.spinner("Generating Interview Questions..."):

            interview_questions = generate_interview_questions()

            st.session_state["interview_questions"] = interview_questions

    # ======================================================
    # Display Questions
    # ======================================================

    if "interview_questions" in st.session_state:

        st.subheader("💼 Generated Interview Questions")

        st.markdown(

            st.session_state["interview_questions"]

        )

        st.download_button(

            label="⬇ Download Interview Questions",

            data=st.session_state["interview_questions"],

            file_name="interview_questions.txt",

            mime="text/plain"

        )

    st.divider()

    # ======================================================
    # Information
    # ======================================================

    st.info("""

### This module generates:

✅ Beginner Level Questions

✅ Intermediate Level Questions

✅ Advanced Level Questions

✅ Scenario-Based Questions

✅ Answers for Every Question

These questions are generated using the uploaded document as context.

""")