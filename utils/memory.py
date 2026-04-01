chat_history = []

def add_memory(user, bot):
    chat_history.append({
        "user": user,
        "bot": bot
    })

def get_memory():
    return chat_history

def clear_memory():
    global chat_history
    chat_history = []