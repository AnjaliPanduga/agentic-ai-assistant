import os

try:
    from groq import Groq
except ImportError:
    Groq = None

def ask_groq(prompt):

    if Groq is None:
        return "⚠️ Groq not installed properly. Please reinstall."

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile"
    )

    return response.choices[0].message.content