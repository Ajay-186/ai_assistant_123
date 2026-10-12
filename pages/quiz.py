import streamlit as st

from services.rag_service import (
    generate_quiz,
    get_pdf_details
)


# ==========================================================
# AI Quiz Generator
# ==========================================================

def show_quiz():

    st.title("🎯 AI Quiz Generator")

    st.markdown(
        "Generate AI-powered quizzes from the uploaded document."
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
    # Quiz Settings
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:

        difficulty = st.selectbox(

            "Difficulty",

            [

                "Easy",

                "Medium",

                "Hard"

            ]

        )

    with col2:

        total_questions = st.selectbox(

            "Number of Questions",

            [

                5,

                10,

                15,

                20

            ]

        )

    st.divider()

    # ======================================================
    # Generate Quiz
    # ======================================================

    if st.button("🎯 Generate Quiz"):

        with st.spinner("Generating Quiz..."):

            quiz = generate_quiz()

            st.session_state["quiz"] = quiz

    # ======================================================
    # Display Quiz
    # ======================================================

    if "quiz" in st.session_state:

        st.subheader("📝 Generated Quiz")

        st.markdown(

            st.session_state["quiz"]

        )

        st.download_button(

            label="⬇ Download Quiz",

            data=st.session_state["quiz"],

            file_name="quiz.txt",

            mime="text/plain"

        )

    st.divider()

    # ======================================================
    # Information
    # ======================================================

    st.info("""

### Quiz Generator

The generated quiz includes:

✅ Multiple Choice Questions

✅ Four Options

✅ Correct Answers

✅ Concept-Based Questions

✅ Revision Questions

The quiz is created using the uploaded document as the knowledge source.

""")