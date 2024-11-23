from rich.console import Console

console = Console()

class Bettor:
    def __init__(self, initial_bankroll, initial_bet):
        self.initial_bankroll = initial_bankroll
        self.bankroll = initial_bankroll
        self.initial_bet = initial_bet
        self.current_bet = initial_bet
        self.history = []
        self.total_wins = 0
        self.total_losses = 0

    def format_number(self, number):
        return f"${number:,.2f}"

    def update(self, outcome):
        if outcome == 'w':
            self.bankroll += self.current_bet
            self.history.append(('W', self.current_bet, self.bankroll))
            self.total_wins += 1
            self.current_bet = self.initial_bet
            console.print(f"[bright_green]🎯 Win! Bet reset to {self.format_number(self.initial_bet)}[/bright_green]")
        else:
            self.bankroll -= self.current_bet
            self.history.append(('L', self.current_bet, self.bankroll))
            self.total_losses += 1
            
            next_bet = self.current_bet * 2
            if next_bet > self.bankroll and self.bankroll > 0:
                console.print("[bright_yellow]⚠️ Warning: Insufficient balance to double the bet![/bright_yellow]")
                self.current_bet = self.bankroll
            elif self.bankroll <= 0:
                console.print("[bright_red]💥 Game Over: Balance depleted![/bright_red]")
                return False
            else:
                self.current_bet = next_bet
                console.print(f"[bright_red]❌ Loss! Bet doubled to {self.format_number(self.current_bet)}[/bright_red]")
        return True