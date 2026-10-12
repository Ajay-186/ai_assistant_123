import streamlit as st

from services.rag_service import (
    summarize,
    get_pdf_details
)


# ==========================================================
# AI Document Summary
# ==========================================================

def show_summary():

    st.title("📄 AI Document Summary")

    st.markdown(
        "Generate an AI-powered summary of the uploaded document."
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
    # Summary Type
    # ======================================================

    summary_type = st.selectbox(

        "Summary Type",

        [

            "Executive Summary",

            "Detailed Summary",

            "Bullet Point Summary",

            "Technical Summary"

        ]

    )

    st.divider()

    # ======================================================
    # Generate Summary
    # ======================================================

    if st.button("📄 Generate Summary"):

        with st.spinner("Generating Summary..."):

            summary = summarize(summary_type)

            st.session_state["summary"] = summary

    # ======================================================
    # Display Summary
    # ======================================================

    if "summary" in st.session_state:

        st.subheader("📄 Generated Summary")

        st.markdown(

            st.session_state["summary"]

        )

        st.download_button(

            label="⬇ Download Summary",

            data=st.session_state["summary"],

            file_name="summary.txt",

            mime="text/plain"

        )

    st.divider()

    # ======================================================
    # Information
    # ======================================================

    st.info("""

### AI Summary

The generated summary includes:

✅ Important Topics

✅ Key Concepts

✅ Main Ideas

✅ Final Conclusion

Different summary styles are available depending on your requirement.

""")