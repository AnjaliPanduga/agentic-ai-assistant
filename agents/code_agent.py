from models.groq_model import ask_groq

def code_agent(user_input):

    prompt = f"""
You are a senior software engineer.

Task:
{user_input}

- Fix errors
- Optimize code
- Explain clearly
"""
    return ask_groq(prompt)