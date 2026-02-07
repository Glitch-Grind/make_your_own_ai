def respond(text: str) -> str:
    text = text.lower()

    if "hello" in text or "hi" in text:
        return "Hello. I am a pre alpha AI."

    if "who are you" in text:
        return "I am an experimental AI built step by step."

    if "help" in text:
        return "I can respond to simple messages for now."

    return "I do not understand yet, but I am learning."
