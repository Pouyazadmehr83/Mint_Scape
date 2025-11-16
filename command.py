import os

class CommandHandler:
    def __init__(self):
        self.commands = {
            "echo": self.cmd_echo,
            "print": self.cmd_echo,
            "hi": self.cmd_hi,
            "hello": self.cmd_hi,
            "hey": self.cmd_hi,
            "clear": self.cmd_clear,   # ← دستور جدید
            "cls": self.cmd_clear      # ← اختیاری، مثل ویندوز
        }

    def run(self, command_line):
        parts = command_line.split()

        if not parts:
            return "No command entered."

        cmd = parts[0]
        args = parts[1:]

        if cmd in self.commands:
            return self.commands[cmd](args)
        else:
            return "Unknown command."

    def cmd_echo(self, args):
        if not args:
            return "Usage: echo <text>"
        return " ".join(args)

    def cmd_hi(self, args):
        return "Hello there!"

    def cmd_clear(self, args):
        # clearscreen Windows = cls, Mac/Linux = clear
        os.system("cls" if os.name == "nt" else "clear")
        return ""   # چیزی چاپ نکند
