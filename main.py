from command import CommandHandler

cmd = CommandHandler()

#print("Type a command (echo, print, hi, hello, hey) - type exit to quit")

while True:
    user_input = input("> ")

    if user_input.lower() in ["exit", "quit"]:
        print("Bye!")
        break

    result = cmd.run(user_input)
    print(result)
