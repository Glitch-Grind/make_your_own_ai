memory = {}


def respond(text: str) -> str:
    lowered = text.lower()

    if "my name is" in lowered:
        name = text.split("my name is")[-1].strip()
        if name:
            memory["name"] = name
            return f"Nice to meet you, {name}."

    if "hello" in lowered or "hi" in lowered:
        if "name" in memory:
            return f"Hello {memory['name']}."
        return "Hello. I am a pre alpha AI."

    if "who are you" in lowered:
        return "I am an experimental AI built step by step."

    if "help" in lowered:
        return "I can respond to simple messages and remember your name."

    return "I do not understand yet, but I am learning."
