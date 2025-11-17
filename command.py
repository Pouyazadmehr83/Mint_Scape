import os
import datetime
from colorama import Fore, Style, init
from banner import Character,Character_M
init(autoreset=True)

class CommandHandler:
    def __init__(self):
        self.commands = {
            "echo":  (self.cmd_echo,  "echo <text>  - print given text"),
            "print": (self.cmd_echo,  "print <text> - same as echo"),
            "hi":    (self.cmd_hi,    "hi/hello/hey - friendly greeting"),
            "hello": (self.cmd_hi,    "hi/hello/hey - friendly greeting"),
            "hey":   (self.cmd_hi,    "hi/hello/hey - friendly greeting"),
            "clear": (self.cmd_clear, "clear screen"),
            "cls":   (self.cmd_clear, "clear screen (alias)"),
            "time":  (self.cmd_time,  "show current time (HH:MM)"),
            "whoami": (self.cmd_whoami, "say name mint"),
            "me":    (self.cmd_showme_m, "show your character"),
            "showme":(self.cmd_showme, "show your character"),
            "help":  (self.cmd_help,  "help [command] - show help"),
        }

    def run(self, command_line):
        parts = command_line.split()

        if not parts:
            return Fore.YELLOW + "No command entered."

        cmd = parts[0]
        args = parts[1:]

        if cmd in self.commands:
            handler, _ = self.commands[cmd]
            return handler(args)
        else:
            return Fore.RED + "Unknown command."

    # -------- Commands ----------

    def cmd_echo(self, args):
        if not args:
            return Fore.YELLOW + "Usage: echo <text>"
        return Fore.CYAN + " ".join(args)

    def cmd_hi(self, args):
        return Fore.GREEN + "Hello there!"

    def cmd_clear(self, args):
        os.system("cls" if os.name == "nt" else "clear")
        return ""

    def cmd_time(self, args):
        x = datetime.datetime.now()
        return Fore.MAGENTA + x.strftime("%H:%M")

    def cmd_whoami(self,args):
        return "mint"

    def cmd_showme_m(self, args):
        Character_M()  
        return None  
    
    def cmd_showme(self, args):
        Character()  
        return None  





    def cmd_help(self, args):
        if args:
            name = args[0]
            if name in self.commands:
                return Fore.BLUE + self.commands[name][1]
            return Fore.RED + f"No help found for: {name}"

        lines = [Fore.YELLOW + "Available commands:"]
        for name, (_, desc) in self.commands.items():
            lines.append(Fore.BLUE + f"  {name:7} - {desc}")
        return "\n".join(lines)
