import os
import shutil

from config import (
    UPLOAD_FOLDER,
    APP_NAME,
    APP_VERSION,
    APP_DESCRIPTION,
    LLM_PROVIDER,
    LLM_MODEL,
    EMBEDDING_MODEL,
    VECTOR_DATABASE,
    RAG_ARCHITECTURE
)

# ==========================================================
# Create Upload Folder
# ==========================================================

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ==========================================================
# Save Uploaded PDF
# ==========================================================

def save_uploaded_file(uploaded_file):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )

    with open(file_path, "wb") as file:

        file.write(uploaded_file.getbuffer())

    return file_path


# ==========================================================
# Delete Uploaded PDF
# ==========================================================

def delete_uploaded_file(file_path):

    if os.path.exists(file_path):

        os.remove(file_path)

        return True

    return False


# ==========================================================
# Clear Upload Folder
# ==========================================================

def clear_upload_folder():

    if os.path.exists(UPLOAD_FOLDER):

        shutil.rmtree(UPLOAD_FOLDER)

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ==========================================================
# Application Information
# ==========================================================

def application_information():

    return {

        "Name": APP_NAME,

        "Description": APP_DESCRIPTION,

        "Version": APP_VERSION,

        "Provider": LLM_PROVIDER,

        "LLM": LLM_MODEL,

        "Embedding Model": EMBEDDING_MODEL,

        "Vector Database": VECTOR_DATABASE,

        "Architecture": RAG_ARCHITECTURE

    }