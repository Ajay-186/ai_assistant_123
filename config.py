import os
from dotenv import load_dotenv

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

# ==========================================================
# Application
# ==========================================================

APP_NAME = "GenAI Workspace"

APP_VERSION = "1.0.0"

APP_DESCRIPTION = "Enterprise AI Research & Knowledge Platform"

# ==========================================================
# Gemini Configuration
# ==========================================================

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

LLM_MODEL = "gemini-2.5-flash"

TEMPERATURE = 0.3

# ==========================================================
# Embedding Model
# ==========================================================

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

EMBEDDING_DIMENSION = 384

# ==========================================================
# FAISS Configuration
# ==========================================================

FAISS_INDEX_PATH = "faiss_db/faiss.index"

FAISS_METADATA_PATH = "faiss_db/metadata.pkl"

# ==========================================================
# Upload Folder
# ==========================================================

UPLOAD_FOLDER = "uploads"

# ==========================================================
# Chunking Configuration
# ==========================================================

CHUNK_SIZE = 500

CHUNK_OVERLAP = 100

# ==========================================================
# Retrieval Configuration
# ==========================================================

TOP_K = 3

# ==========================================================
# Supported Files
# ==========================================================

SUPPORTED_FILE_TYPES = [

    "pdf"

]

# ==========================================================
# Application Information
# ==========================================================

VECTOR_DATABASE = "FAISS"

RAG_ARCHITECTURE = "Manual RAG"

EMBEDDING_PROVIDER = "Sentence Transformers"

LLM_PROVIDER = "Google Gemini"