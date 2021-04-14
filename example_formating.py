import time
from  rich.console import Console
from  rich.style import Style
from  rich.theme import Theme
from  rich.text import Text
from  rich.prompt import Prompt
from  rich.panel import Panel
from  rich.console import RenderGroup
from  rich.markdown import Markdown
from  rich.progress import track
from  rich.progress import Progress


def example_text_format():
    console = Console(width=20)
    console.print("[uu bold red] Hello[/] [blue]world[/blue]Rich")
    style = "bold white on green"
    console.print("Rich", style=style)
    console.print("Rich", style=style, justify="left")
    console.print("Rich", style=style, justify="center")
    console.print("Rich", style=style, justify="rigth")
    console = Console(width=14)
    supercali = "supercaliflaglisticexpialidocios      asjdlakj a jalkj aldkja ljaldkj lakjd lakjla kjdlkj d"
    overflow_method = ["fold", "crop", "ellipsis"]
    for overflow in overflow_method:
        console.rule(overflow)
        console.print(supercali, overflow=overflow_method, style="bold blue")
        console.print()
    console = Console()
    console.input("What is [i]your[/i] [bold red]name[/]? :smiley: ")
    style_allert = "blink bold red underline on white"
    style_danger = Style(color="red", blink=True, bold=True)
    console.print("ALLERT", style=style_allert)
    console.print("ALLERT", style=style_danger)
    console.print("GOOGLE", style="link https://google.com")
    console = Console(theme=Theme({"repr.number": "bold green blink"}))
    console.print("128 is 128 adasd  sad ad a d")
    console = Console()
    console = Console()
    text = Text("Hello, world!")
    text.stylize("bold magenta", 0, 8)
    console.print(text)


def example_status():
    def do_work():
        for i in range(2):
            print(i)
            time.sleep(1)
    with console.status("Monkey around...", spinner="monkey"):
        do_work()


def example_exception():
    try:
        print(1/0)
    except:
        console.print_exception()



def input():
    name = Prompt.ask("Enter your name", default="Paul Atreides")
    print(name)
    name = Prompt.ask("Enter your name", choices=["test", "adad", "adaldkj"],default="Paul Atreides")
    print(name)


def example_panel():
    panel_group = RenderGroup(
        Panel("Hello", style="red on blue"),
        Panel("world", style="on red" ),
        Panel.fit("world", style="on red" ),
        Panel("[red] world", title="Welcom" )
    )

    console.print(Panel(panel_group))

    MARKDOWN = """
    # Title
    Test
    1. kasd,.ansd
    2. asd asdmadm .


    """
    console = Console()
    md = Markdown(MARKDOWN)
    console.print(md)

def example_track():
    for n in track(range(100), description="Processing..."):
        time.sleep(0.03)




def example_progress():
    with Progress() as progress:
        task1 = progress.add_task("[red]Downloading...", total=100)
        task2 = progress.add_task("[red]Processing...", total=100)
        task3 = progress.add_task("[red]Cooking...", total=100)
        while not progress.finished:
            progress.update(task1, advance=0.5)
            progress.update(task2, advance=0.3)
            progress.update(task3, advance=0.9)
            time.sleep(0.02)
        
def example_read_file():
    from rich.syntax import Syntax
    console = Console()
    with open("example_formating.py", "r") as f:
        syntax = Syntax(f.read(), "python", line_numbers=True)
    console.print(syntax)
