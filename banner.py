from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from time import sleep

console = Console()

def type_print(text, delay=0.03):
    """نمایش متن با افکت تایپ"""
    for char in text:
        console.print(char, end="", soft_wrap=True, highlight=False)
        sleep(delay)
    console.print()  # newline

def show_banner():
    banner_text = """
    MINT SCAPE
      __  __ _       _   ____  _____ ____  
     |  \/  (_)_ __ | |_/ ___|| ____|  _ \ 
     | |\/| | | '_ \| __\___ \|  _| | | | |
     | |  | | | | | | |_ ___) | |___| |_| |
     |_|  |_|_|_| |_|\__|____/|_____|____/
    """

    character = r"""
    (\_._/)   
    ( o_o )   
    />🌸   ← Mint runs!
   /  |       
  ^^ ^^
    """


    console.print(Panel(Text(banner_text, justify="center", style="bold cyan"), expand=False))
    type_print(character)



def Character():
    character = r"""
    (\_._/)   
    ( o_o )   
    />🌸   ← hi honey!
   /  |       
  ^^ ^^
    """
    print(character)


def Character_M():
    character = r"""
    (\_._/)   
    ( o_o )   
    />🌸   ← meeaowwww!
   /  |       
  ^^ ^^
    """
    print(character)



 