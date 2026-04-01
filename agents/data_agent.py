from models.gemini_model import ask_gemini

def data_agent(user_input):

    prompt = f"""
You are a data analyst.

Analyze the request:
{user_input}

Give insights and suggestions.
"""
    return ask_gemini(prompt)