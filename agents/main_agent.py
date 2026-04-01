from models.gemini_model import ask_gemini
from models.groq_model import ask_groq

def agent_decision(user_input, file_content=None):

    # 🔥 If file is present → use Gemini (better for analysis)
    if file_content:
        prompt = f"""
You are an AI assistant.

User Query:
{user_input}

File Content:
{file_content}

Answer clearly based on the file.
"""
        return ask_gemini(prompt)

    # 🔥 Otherwise → fast response using Groq
    return ask_groq(user_input)