import google.generativeai as genai

from config import GOOGLE_API_KEY
from config import LLM_MODEL
from config import TEMPERATURE


# ==========================================================
# Configure Gemini
# ==========================================================

genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {

    "temperature": TEMPERATURE,

    "top_p": 1,

    "top_k": 1,

    "max_output_tokens": 2048

}

gemini_model = genai.GenerativeModel(

    model_name=LLM_MODEL,

    generation_config=generation_config

)


# ==========================================================
# Generate AI Response
# ==========================================================

def generate_answer(prompt):

    try:

        response = gemini_model.generate_content(prompt)

        return {

            "success": True,

            "response": response.text

        }

    except Exception as e:

        return {

            "success": False,

            "response": str(e)

        }


# ==========================================================
# Health Check
# ==========================================================

def check_connection():

    try:

        response = gemini_model.generate_content("Hello")

        return True

    except:

        return False


# ==========================================================
# Model Information
# ==========================================================

def get_model_information():

    return {

        "provider": "Google",

        "model": LLM_MODEL,

        "temperature": TEMPERATURE,

        "max_tokens": 2048

    }