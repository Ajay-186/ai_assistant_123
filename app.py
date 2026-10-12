import streamlit as st

from config import APP_NAME

# ===========================
# Import Pages
# ===========================

from pages.dashboard import show_dashboard
from pages.documents import show_documents
from pages.chat import show_chat
from pages.summary import show_summary
from pages.notes import show_notes
from pages.quiz import show_quiz
from pages.flashcards import show_flashcards
from pages.interview import show_interview
from pages.semantic_search import show_semantic_search
from pages.embeddings_view import show_embeddings
from pages.vector_database import show_vector_database
from pages.analytics import show_analytics
from pages.settings import show_settings

# ===========================
# Streamlit Config
# ===========================

st.set_page_config(

    page_title=APP_NAME,

    page_icon="🚀",

    layout="wide",

    initial_sidebar_state="expanded"

)

# ===========================
# Sidebar
# ===========================

st.sidebar.title("🚀 GenAI Workspace")

pages = {

    "🏠 Dashboard": show_dashboard,

    "📂 Documents": show_documents,

    "💬 AI Chat": show_chat,

    "📄 Summary": show_summary,

    "📝 Notes": show_notes,

    "🎯 Quiz": show_quiz,

    "🃏 Flashcards": show_flashcards,

    "❓ Interview Questions": show_interview,

    "🔍 Semantic Search": show_semantic_search,

    "🧠 Embeddings": show_embeddings,

    "🗄 Vector Database": show_vector_database,

    "📊 Analytics": show_analytics,

    "⚙ Settings": show_settings

}

selected_page = st.sidebar.radio(

    "Navigation",

    list(pages.keys())

)

# ===========================
# Load Page
# ===========================

pages[selected_page]()