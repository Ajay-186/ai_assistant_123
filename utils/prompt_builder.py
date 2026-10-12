# ==========================================================
# Build RAG Prompt
# ==========================================================

def build_prompt(question, retrieved_chunks):

    context = "\n\n".join(

        chunk["document"] if isinstance(chunk, dict) else str(chunk)

        for chunk in retrieved_chunks

    )

    prompt = f"""
You are an expert AI Research Assistant.

Instructions:

- Answer ONLY using the provided context.
- Do not make up information.
- If the answer is not present in the context, reply exactly:

"I couldn't find the answer in the uploaded document."

- Keep the answer clear and well structured.
- Use bullet points whenever appropriate.

====================================================

CONTEXT

{context}

====================================================

QUESTION

{question}

====================================================

ANSWER

"""

    return prompt


# ==========================================================
# Summary Prompt
# ==========================================================

def build_summary_prompt(context):

    return f"""
You are an expert document summarizer.

Summarize the following document.

Include:

• Overview

• Important Topics

• Key Concepts

• Final Conclusion

====================================================

DOCUMENT

{context}

====================================================

SUMMARY

"""


# ==========================================================
# Notes Prompt
# ==========================================================

def build_notes_prompt(context):

    return f"""
Generate detailed study notes.

Include:

1. Headings

2. Important Concepts

3. Definitions

4. Key Points

5. Revision Notes

====================================================

DOCUMENT

{context}

====================================================

NOTES

"""


# ==========================================================
# Quiz Prompt
# ==========================================================

def build_quiz_prompt(context):

    return f"""
Generate 10 Multiple Choice Questions.

Each question should contain:

Question

4 Options

Correct Answer

====================================================

DOCUMENT

{context}

====================================================

QUIZ

"""


# ==========================================================
# Flashcards Prompt
# ==========================================================

def build_flashcards_prompt(context):

    return f"""
Generate flashcards.

Format

Question:

Answer:

====================================================

DOCUMENT

{context}

====================================================

FLASHCARDS

"""


# ==========================================================
# Interview Prompt
# ==========================================================

def build_interview_prompt(context):

    return f"""
Generate interview questions.

Create

• Beginner

• Intermediate

• Advanced

Provide answers as well.

====================================================

DOCUMENT

{context}

====================================================

INTERVIEW QUESTIONS

"""


# ==========================================================
# Custom Prompt
# ==========================================================

def build_custom_prompt(task, context):

    return f"""
Perform the following task.

Task:

{task}

====================================================

DOCUMENT

{context}

====================================================

RESULT

"""