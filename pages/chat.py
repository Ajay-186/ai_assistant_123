import streamlit as st
from datetime import datetime

from services.rag_service import (
    chat,
    get_pdf_details
)


# ==========================================================
# AI Chat Page
# ==========================================================

def show_chat():

    st.title("💬 AI Chat")

    st.markdown(
        "Ask questions about your uploaded document."
    )

    pdf = get_pdf_details()

    if pdf is None:

        st.warning("📂 Please upload a PDF first.")

        return

    st.success(f"Current Document : {pdf['file_name']}")

    st.divider()

    # ======================================================
    # Session State
    # ======================================================

    if "messages" not in st.session_state:

        st.session_state.messages = []

    # ======================================================
    # Display Previous Messages
    # ======================================================

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

            st.caption(message["time"])

    # ======================================================
    # Chat Input
    # ======================================================

    question = st.chat_input("Ask anything about your PDF...")

    if question:

        current_time = datetime.now().strftime("%I:%M %p")

        # User Message
        st.session_state.messages.append({

            "role": "user",

            "content": question,

            "time": current_time

        })

        with st.chat_message("user"):

            st.markdown(question)

            st.caption(current_time)

        # AI Response
        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                answer = chat(question)

                st.markdown(answer)

                st.caption(current_time)

        st.session_state.messages.append({

            "role": "assistant",

            "content": answer,

            "time": current_time

        })

    st.divider()

    # ======================================================
    # Clear Chat
    # ======================================================

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()