def is_safe(text: str) -> bool:
    if not text:
        return False

    banned_words = [
        "kill",
        "die",
        "hack",
        "virus",
        "trojan",
        "RAT",
    ]

    lowered = text.lower()

    for word in banned_words:
        if word in lowered:
            return False

    return True
