from models.groq_model import ask_groq

def debug_code(code):
    prompt = f"""
You are a senior developer.

1. Find errors
2. Fix code
3. Explain clearly

Code:
{code}
"""
    return ask_groq(prompt)