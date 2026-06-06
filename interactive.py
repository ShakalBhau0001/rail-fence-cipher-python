from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.text import Text

console = Console()


def rail_fence_encrypt(text, rails):
    text = text.replace(" ", "")
    fence = [[] for _ in range(rails)]
    row = 0
    direction = 1

    for char in text:
        fence[row].append(char)
        row += direction

        if row == 0 or row == rails - 1:
            direction *= -1

    return "".join("".join(r) for r in fence)


def rail_fence_decrypt(cipher, rails):
    pattern = [[] for _ in range(rails)]
    row = 0
    direction = 1

    for _ in cipher:
        pattern[row].append("*")
        row += direction
        if row == 0 or row == rails - 1:
            direction *= -1

    index = 0
    for r in range(rails):
        for c in range(len(pattern[r])):
            pattern[r][c] = cipher[index]
            index += 1

    result = []
    row = 0
    direction = 1

    for _ in cipher:
        result.append(pattern[row].pop(0))
        row += direction
        if row == 0 or row == rails - 1:
            direction *= -1

    return "".join(result)


def main():
    console.clear()
    console.print(
        Panel.fit(
            "[bold cyan]🚆 Rail Fence Cipher Tool[/bold cyan]",
            border_style="cyan",
        )
    )

    choice = Prompt.ask(
        "\n[bold yellow]Choose mode[/bold yellow]", choices=["E", "D"], default="E"
    )

    message = Prompt.ask("[bold yellow]Enter message[/bold yellow]")
    rails = IntPrompt.ask("[bold yellow]Enter number of rails[/bold yellow]")

    if rails < 2:
        console.print("[bold red]❌ Rails must be at least 2![/bold red]")
        return

    if choice == "E":
        result = rail_fence_encrypt(message, rails)
        title = "Encrypted Message"
        style = "bold green"

    else:
        result = rail_fence_decrypt(message, rails)
        title = "Decrypted Message"
        style = "bold magenta"

    console.print(
        Panel(f"[{style}]{result}[/{style}]", title=f"✨ {title}", border_style="blue")
    )


if __name__ == "__main__":
    main()
