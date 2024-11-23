from bettor import Bettor
from history_view import HistoryView
from statistics_view import StatisticsView
from rich.console import Console
import os

# Detect operating system and import appropriate library
if os.name == 'nt':  # Windows
    import msvcrt
    def wait_for_key():
        console.print("\nPress any key to return to the menu...")
        msvcrt.getch()
else:  # Linux/Mac
    from getch import getch
    def wait_for_key():
        console.print("\nPress any key to return to the menu...")
        getch()

console = Console()

def main():
    # Initialize initial values
    initial_bankroll = 1000
    initial_bet = 10
    bettor = Bettor(initial_bankroll, initial_bet)

    while True:
        # Display the menu
        console.clear()
        console.print(f"[bright_green]💰 Balance: {bettor.format_number(bettor.bankroll)}[/bright_green]")
        console.print(f"[bright_cyan]🎲 Current bet: {bettor.format_number(bettor.current_bet)}[/bright_cyan]\n")
        
        console.print("[bright_yellow]Choose an action:[/bright_yellow]")
        console.print("[bright_white]✅ [W] Win[/bright_white]")
        console.print("[bright_white]❌ [L] Loss[/bright_white]")
        console.print("[bright_white]📜 [H] History[/bright_white]")
        console.print("[bright_white]📊 [S] Statistics[/bright_white]")
        console.print("[bright_white]🚪 [E] Exit[/bright_white]")

        # Get the user's choice
        choice = input("\nEnter your choice: ").lower()

        # Handle the user's choice
        if choice == 'w':
            if not bettor.update('w'):
                break
        elif choice == 'l':
            if not bettor.update('l'):
                break
        elif choice == 'h':
            console.clear()  # Hide the menu
            HistoryView.display(bettor.history)
            wait_for_key()  # Wait for any key press
        elif choice == 's':
            console.clear()  # Hide the menu
            StatisticsView.display(bettor)
            wait_for_key()  # Wait for any key press
        elif choice == 'e':
            break
        else:
            console.print("[bright_red]Invalid choice! Please try again.[/bright_red]")
            wait_for_key()  # Wait for any key press before retrying

if __name__ == "__main__":
    main()