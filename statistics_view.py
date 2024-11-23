from rich.panel import Panel
from rich.console import Console

console = Console()

class StatisticsView:
    @staticmethod
    def display(bettor):
        total_bets = bettor.total_wins + bettor.total_losses
        roi = ((bettor.bankroll - bettor.initial_bankroll) / bettor.initial_bankroll * 100) if total_bets > 0 else 0

        stats_panel = Panel(
            f"""[bright_white]🎲 Total bets: {total_bets}[/bright_white]
[bright_cyan]✅ Wins: {bettor.total_wins} | ❌ Losses: {bettor.total_losses}[/bright_cyan]
[bright_magenta]📈 ROI: {roi:.2f}%[/bright_magenta]
[bright_green]💰 Balance: {bettor.format_number(bettor.bankroll)}[/bright_green]""",
            title="📊 Statistics",
            border_style="bright_blue",
            expand=False
        )
        console.print(stats_panel)