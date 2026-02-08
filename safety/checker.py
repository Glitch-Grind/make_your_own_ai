from datetime import datetime


BANNED_WORDS = [
    "kill",
    "die",
    "hack",
    "virus"
]


def log_blocked_input(text: str, reason: str) -> None:
    with open("safety_log.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.now().isoformat()
        file.write(f"{timestamp} | {reason} | {text}\n")


def check_safety(text: str) -> tuple[bool, str]:
    if not text.strip():
        return False, "empty input"

    lowered = text.lower()

    for word in BANNED_WORDS:
        if word in lowered:
            log_blocked_input(text, f"banned word: {word}")
            return False, f"contains banned word '{word}'"

    return True, "ok"
