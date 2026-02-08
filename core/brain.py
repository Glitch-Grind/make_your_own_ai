import json
from pathlib import Path
from core.personality import style

MEMORY_FILE = Path("data/memory.json")

# load memory
if MEMORY_FILE.exists():
    try:
        memory = json.loads(MEMORY_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        memory = {}
else:
    memory = {}


def save_memory() -> None:
    MEMORY_FILE.write_text(
        json.dumps(memory, indent=2),
        encoding="utf-8"
    )


def respond(text: str) -> str:
    lowered = text.lower()

    if "my name is" in lowered:
        name = text.split("my name is", 1)[-1].strip()
        if name:
            memory["name"] = name
            save_memory()
            return style(f"Nice to meet you, {name}.")
        return style("I did not catch your name.")

    if "hello" in lowered or "hi" in lowered:
        if "name" in memory:
            return style(f"Hello {memory['name']}.")
        return style("Hello. I am a pre alpha AI.")

    if "who are you" in lowered:
        return style("I am a small AI built step by step.")

    if "help" in lowered:
        return style(
            "I can talk, remember simple things, and keep conversations safe."
        )

    return style("I do not understand yet, but I am learning.")
