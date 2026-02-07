from core.brain import respond
from safety.checker import is_safe


def main():
    user_input = input("You: ")

    if not is_safe(user_input):
        print("AI: Input rejected by safety system.")
        return

    reply = respond(user_input)
    print("AI:", reply)


if __name__ == "__main__":
    main()
