from core.brain import respond
from safety.checker import check_safety


def main():
    print("AI started. Type 'exit' to quit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("AI: Goodbye.")
            break

        allowed, reason = check_safety(user_input)

        if not allowed:
            print(f"AI: Input blocked because {reason}.")
            continue

        reply = respond(user_input)
        print("AI:", reply)


if __name__ == "__main__":
    main()
