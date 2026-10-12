import os
from pypdf import PdfReader


# ==========================================================
# Read PDF
# ==========================================================

def read_pdf(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    pages = []

    total_pages = len(reader.pages)

    for page_number, page in enumerate(reader.pages, start=1):

        page_text = page.extract_text()

        if page_text:

            text += page_text + "\n"

            pages.append({

                "page_number": page_number,

                "text": page_text,

                "characters": len(page_text)

            })

    metadata = reader.metadata

    return {

        "file_name": os.path.basename(pdf_path),

        "file_path": pdf_path,

        "pages": total_pages,

        "characters": len(text),

        "preview": text[:500],

        "metadata": metadata,

        "text": text,

        "page_data": pages

    }


# ==========================================================
# PDF Statistics
# ==========================================================

def get_pdf_statistics(pdf):

    return {

        "file_name": pdf["file_name"],

        "pages": pdf["pages"],

        "characters": pdf["characters"]

    }


# ==========================================================
# Get Page Text
# ==========================================================

def get_page_text(pdf, page_number):

    for page in pdf["page_data"]:

        if page["page_number"] == page_number:

            return page["text"]

    return ""


# ==========================================================
# Get Page Preview
# ==========================================================

def get_page_preview(pdf):

    preview = []

    for page in pdf["page_data"]:

        preview.append({

            "Page": page["page_number"],

            "Characters": page["characters"],

            "Preview": page["text"][:120]

        })

    return preview