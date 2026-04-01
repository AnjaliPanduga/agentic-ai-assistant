def detect_task(user_input):
    text = user_input.lower()

    if "code" in text or "error" in text or "bug" in text:
        return "code"

    elif "analyze" in text or "data" in text:
        return "data"

    elif "file" in text:
        return "file"

    return "general"