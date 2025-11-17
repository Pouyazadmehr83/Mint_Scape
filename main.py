from command import CommandHandler
from banner import show_banner
def main():
    
    show_banner()

    handler = CommandHandler()

    print("=== Mint Scape CLI ===")
    print("Type 'help' for commands.\n")


    while True:
        try:
            user_input = input("> ")
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        result = handler.run(user_input)
        if result is not None:
            print(result)

        if user_input.strip() == "exit":
            print("Bye!")
            break


if __name__ == "__main__":
    main()
