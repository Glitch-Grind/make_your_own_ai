from core.brain import respond
from safety.checker import is_safe


def main():
    print("AI started. Type 'exit' to quit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("AI: Goodbye.")
            break

        if not is_safe(user_input):
            print("AI: Input rejected by safety system.")
            continue

        reply = respond(user_input)
        print("AI:", reply)


if __name__ == "__main__":
    main()
