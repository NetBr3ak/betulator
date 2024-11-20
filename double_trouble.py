import sys

# Text effects and colors
RESET = "\033[0m"
BOLD = "\033[1m"

# Text colors (optimized for a black background)
HEADER = "\033[93m"  # Bright Yellow
SUCCESS = "\033[92m"  # Bright Green
FAILURE = "\033[91m"  # Bright Red
WARNING = "\033[95m"  # Bright Magenta
INFO = "\033[96m"  # Cyan
BET_BALANCE = "\033[94m"  # Bright Blue
WHITE = "\033[97m"  # Bright White

# Emojis
EMOJI_SUCCESS = "✅"
EMOJI_FAILURE = "❌"
EMOJI_WARNING = "⚠️"
EMOJI_INFO = "📘"
EMOJI_CHART = "📈"
EMOJI_HIST = "📜"
EMOJI_STATS = "📊"
EMOJI_EXIT = "🚪"
EMOJI_BET = "🎲"
EMOJI_BANKROLL = "💰"

def color_text(text, color, bold=False):
    if bold:
        return f"{BOLD}{color}{text}{RESET}"
    return f"{color}{text}{RESET}"

def clear_console():
    print("\033[2J\033[H", end='')

class MartingaleStrategy:
    def __init__(self, initial_bet, bankroll):
        self.initial_bet = initial_bet
        self.current_bet = initial_bet
        self.bankroll = bankroll
        self.bankroll_initial = bankroll
        self.current_double = 0
        self.history = []
        self.total_wins = 0
        self.total_losses = 0
        self.total_bet_amount = 0
        self.bankroll_history = [bankroll]

    def update(self, outcome):
        outcome = outcome.lower()
        if outcome not in ['w', 'l']:
            sys.stdout.write(color_text(f"{EMOJI_FAILURE} Invalid outcome. Use 'w' (Win) or 'l' (Loss).\n\n", FAILURE, bold=True))
            return False

        self.total_bet_amount += self.current_bet

        if outcome == 'w':
            self.bankroll += self.current_bet
            self.history.append(('W', self.current_bet, self.bankroll))
            self.total_wins += 1
            self.current_bet = self.initial_bet
            self.current_double = 0
            sys.stdout.write(color_text(f"{EMOJI_SUCCESS} Win! Bet reset to {self.format_number(self.initial_bet)}.\n\n", SUCCESS))
        else:
            self.bankroll -= self.current_bet
            self.history.append(('L', self.current_bet, self.bankroll))
            self.total_losses += 1
            self.current_double += 1

            next_bet = self.current_bet * 2
            if next_bet > self.bankroll and self.bankroll > 0:
                sys.stdout.write(color_text(f"{EMOJI_WARNING} Insufficient balance to double the bet. Bet set to {self.format_number(self.bankroll)}.\n\n", WARNING, bold=True))
                self.current_bet = self.bankroll
            elif self.bankroll <= 0:
                sys.stdout.write(color_text(f"{EMOJI_FAILURE} Balance depleted. Game over.\n\n", FAILURE, bold=True))
                return False
            else:
                self.current_bet = next_bet
                sys.stdout.write(color_text(f"{EMOJI_FAILURE} Loss! Bet doubled to {self.format_number(self.current_bet)}.\n\n", FAILURE))

        self.bankroll_history.append(self.bankroll)
        return True

    def display_history(self):
        if not self.history:
            sys.stdout.write(color_text(f"\n{EMOJI_INFO} Bet history is empty.\n\n", INFO, bold=True))
            return

        sys.stdout.write(color_text(f"\n{EMOJI_HIST} === Bet History ===\n", HEADER, bold=True))
        no_width, result_width, bet_width, balance_width = 4, 7, 12, 14
        header = (
            f"{color_text('No', HEADER, bold=True):<{no_width}}| "
            f"{color_text('Result', HEADER, bold=True):<{result_width}}| "
            f"{color_text('Bet', HEADER, bold=True):<{bet_width}}| "
            f"{color_text('Balance', HEADER, bold=True):<{balance_width}}\n"
        )
        sys.stdout.write(header)
        sys.stdout.write(color_text("-" * (no_width + result_width + bet_width + balance_width + 9) + "\n", INFO))

        for i, (outcome, bet, bankroll) in enumerate(self.history, 1):
            outcome_colored = color_text(f"{EMOJI_SUCCESS} W" if outcome == 'W' else f"{EMOJI_FAILURE} L", SUCCESS if outcome == 'W' else FAILURE)
            line = (
                f"{i:<{no_width}}| "
                f"{outcome_colored:<{result_width}}| "
                f"{color_text(self.format_number(bet), BET_BALANCE):<{bet_width}}| "
                f"{color_text(self.format_number(bankroll), BET_BALANCE):<{balance_width}}\n"
            )
            sys.stdout.write(line)

        sys.stdout.write(color_text("=" * (no_width + result_width + bet_width + balance_width + 9) + "\n\n", INFO))

    def display_statistics(self):
        total_bets = self.total_wins + self.total_losses
        roi = ((self.bankroll - self.bankroll_initial) / self.total_bet_amount) * 100 if self.total_bet_amount else 0

        sys.stdout.write(color_text(f"\n{EMOJI_STATS} === Statistics ===\n", HEADER, bold=True))
        sys.stdout.write(color_text(f"{EMOJI_BANKROLL} Total bets: {total_bets}\n", WHITE))
        sys.stdout.write(color_text(f"{EMOJI_SUCCESS} Wins: {self.total_wins}\n", SUCCESS))
        sys.stdout.write(color_text(f"{EMOJI_FAILURE} Losses: {self.total_losses}\n", FAILURE))
        sys.stdout.write(color_text(f"{EMOJI_BET} Total bet amount: {self.format_number(self.total_bet_amount)}\n", BET_BALANCE))
        sys.stdout.write(color_text(f"{EMOJI_INFO} ROI (Return on Investment): {roi:.2f}%\n", INFO))
        sys.stdout.write(color_text(f"{EMOJI_BANKROLL} Balance: {self.format_number(self.bankroll)}\n", BET_BALANCE))
        sys.stdout.write(color_text("====================\n\n", INFO))

    def display_chart(self):
        if len(self.bankroll_history) < 2:
            sys.stdout.write(color_text(f"\n{EMOJI_INFO} Not enough data for the chart.\n\n", INFO, bold=True))
            return

        sys.stdout.write(color_text(f"\n{EMOJI_CHART} === Bankroll Chart ===\n", HEADER, bold=True))

        max_bankroll = max(self.bankroll_history)
        min_bankroll = min(self.bankroll_history)
        range_bankroll = max_bankroll - min_bankroll or 1
        chart_width = 50
        step = range_bankroll / chart_width

        for bankroll in self.bankroll_history:
            bar_length = int((bankroll - min_bankroll) / step)
            bar = "█" * bar_length
            label = f"{self.format_number(bankroll):>10}"
            sys.stdout.write(color_text(f"{label} | {bar}\n", SUCCESS if bankroll > 0 else FAILURE))

        sys.stdout.write(color_text(" " * 12 + "+" + "-" * chart_width + "\n", INFO))
        sys.stdout.write(color_text(" " * 12 + "0".ljust(chart_width // 2) + f"{len(self.bankroll_history)}\n", INFO))
        sys.stdout.write(color_text("====================\n\n", HEADER, bold=True))

    @staticmethod
    def format_number(value):
        return f"{value:,.2f}".replace(",", " ")

def get_positive_float(prompt):
    while True:
        try:
            sys.stdout.write(color_text(prompt, BET_BALANCE))
            sys.stdout.flush()
            value_str = sys.stdin.readline().strip()
            value = float(value_str)
            if value <= 0:
                sys.stdout.write(color_text(f"{EMOJI_WARNING} Value must be greater than zero.\n\n", WARNING, bold=True))
                continue
            return value
        except ValueError:
            sys.stdout.write(color_text(f"{EMOJI_FAILURE} Invalid value. Please try again.\n\n", FAILURE, bold=True))

def display_header():
    header_text = "Martingale Strategy for European Roulette"
    sys.stdout.write(color_text(header_text + "\n\n", HEADER, bold=True))

def display_controls():
    sys.stdout.write(color_text(f"{EMOJI_SUCCESS} Enter 'w' (Win)\n", SUCCESS))
    sys.stdout.write(color_text(f"{EMOJI_FAILURE} Enter 'l' (Loss)\n", FAILURE))
    sys.stdout.write(color_text(f"{EMOJI_HIST} Enter 'h' (History)\n", INFO))
    sys.stdout.write(color_text(f"{EMOJI_STATS} Enter 's' (Statistics)\n", BET_BALANCE))
    sys.stdout.write(color_text(f"{EMOJI_CHART} Enter 'c' (Chart)\n", WARNING))
    sys.stdout.write(color_text(f"{EMOJI_EXIT} Enter 'e' (Exit)\n\n", WHITE))

def main():
    clear_console()
    display_header()

    initial_bet = get_positive_float(f"{EMOJI_BET} Initial bet (e.g., 10): ")
    bankroll = get_positive_float(f"{EMOJI_BANKROLL} Starting balance (e.g., 1000): ")

    bettor = MartingaleStrategy(initial_bet, bankroll)

    sys.stdout.write(color_text(f"{EMOJI_WARNING} Martingale strategy without doubling limits.\n\n", WARNING, bold=True))

    while True:
        clear_console()
        display_header()
        display_controls()

        sys.stdout.write(color_text(f"{EMOJI_BANKROLL} Balance: {bettor.format_number(bettor.bankroll)}\n", BET_BALANCE))
        sys.stdout.write(color_text(f"{EMOJI_BET} Current bet: {bettor.format_number(bettor.current_bet)}\n\n", BET_BALANCE))

        sys.stdout.write(color_text(f"{EMOJI_INFO} Enter outcome ('w', 'l'), 'h', 's', 'c', 'e': ", INFO))
        sys.stdout.flush()
        outcome = sys.stdin.readline().strip().lower()

        if outcome == 'e':
            sys.stdout.write(color_text(f"\n{EMOJI_EXIT} Exiting the game...\n\n", HEADER, bold=True))
            break
        elif outcome == 'h':
            clear_console()
            bettor.display_history()
            input(color_text("Press Enter to continue...", INFO))
        elif outcome == 's':
            clear_console()
            bettor.display_statistics()
            input(color_text("Press Enter to continue...", INFO))
        elif outcome == 'c':
            clear_console()
            bettor.display_chart()
            input(color_text("Press Enter to continue...", INFO))
        elif outcome in ['w', 'l']:
            if not bettor.update(outcome):
                break
            input(color_text("Press Enter to continue...", INFO))
        else:
            sys.stdout.write(color_text(f"{EMOJI_FAILURE} Invalid command. Try again.\n\n", FAILURE, bold=True))
            input(color_text("Press Enter to continue...", INFO))

    sys.stdout.write(color_text(f"=== {EMOJI_HIST} Final Bet History ===\n", HEADER, bold=True))
    bettor.display_history()
    bettor.display_statistics()
    sys.stdout.write(color_text(f"Thank you! Good luck! {EMOJI_SUCCESS}\n\n", SUCCESS))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write(color_text(f"\n{EMOJI_FAILURE} Program terminated.\n", FAILURE, bold=True))
        sys.exit()
