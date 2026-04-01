from models.gemini_model import ask_gemini

def file_agent(user_input, file_content):

    prompt = f"""
You are an AI assistant.

User Request:
{user_input}

File Content:
{file_content}

Extract insights and answer clearly.
"""
    return ask_gemini(prompt)