from rich.table import Table
from rich.console import Console

console = Console()

class HistoryView:
    @staticmethod
    def display(history):
        table = Table(title="📜 Bet History", border_style="bright_blue")
        table.add_column("Round", justify="center")
        table.add_column("Outcome", justify="center")
        table.add_column("Bet Amount", justify="right")
        table.add_column("Balance", justify="right")

        for i, (outcome, bet, balance) in enumerate(history, 1):
            outcome_text = "[bright_green]✅ Win[/bright_green]" if outcome == 'W' else "[bright_red]❌ Loss[/bright_red]"
            table.add_row(str(i), outcome_text, f"${bet:,.2f}", f"${balance:,.2f}")
        console.print(table)