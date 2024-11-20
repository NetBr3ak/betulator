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
    """
    Adds color and optional bold styling to text for terminal output.
    """
    if bold:
        return f"{BOLD}{color}{text}{RESET}"
    return f"{color}{text}{RESET}"

def clear_console():
    """
    Clears the terminal screen to maintain clean output.
    """
    print("\033[2J\033[H", end='')

class MartingaleStrategy:
    def __init__(self, initial_bet, bankroll):
        """
        Initializes the Martingale strategy with the given initial bet and bankroll.
        Tracks historical data, win/loss statistics, and bankroll changes.
        """
        self.initial_bet = initial_bet
        self.current_bet = initial_bet
        self.bankroll = bankroll
        self.bankroll_initial = bankroll
        self.current_double = 0
        self.history = []  # Tracks each round's outcome, bet, delta, and resulting balance.
        self.total_wins = 0
        self.total_losses = 0
        self.total_bet_amount = 0
        self.bankroll_history = [bankroll]  # Keeps a history of the bankroll for chart generation.

    def update(self, outcome):
        """
        Updates the game state based on the outcome ('w' for win, 'l' for loss).
        Handles bet adjustments, bankroll updates, and tracking win/loss stats.
        """
        outcome = outcome.lower()
        if outcome not in ['w', 'l']:
            sys.stdout.write(color_text(f"{EMOJI_FAILURE} Invalid outcome. Use 'w' (Win) or 'l' (Loss).\n\n", FAILURE, bold=True))
            return False

        # Track the total amount bet so far
        self.total_bet_amount += self.current_bet

        if outcome == 'w':
            # Win case: Add current bet to bankroll, reset to initial bet
            self.bankroll += self.current_bet
            self.history.append(('W', self.current_bet, self.current_bet, self.bankroll))
            self.total_wins += 1
            self.current_bet = self.initial_bet
            self.current_double = 0
            sys.stdout.write(color_text(f"{EMOJI_SUCCESS} You won! Bet reset to {self.format_number(self.initial_bet)}.\n", SUCCESS, bold=True))
        else:
            # Loss case: Subtract current bet from bankroll, double the bet if possible
            self.bankroll -= self.current_bet
            self.history.append(('L', self.current_bet, -self.current_bet, self.bankroll))
            self.total_losses += 1
            self.current_double += 1

            # Adjust the next bet or end the game if out of balance
            next_bet = self.current_bet * 2
            if next_bet > self.bankroll and self.bankroll > 0:
                self.current_bet = self.bankroll
                sys.stdout.write(color_text(f"{EMOJI_WARNING} Insufficient balance to double. Bet set to {self.format_number(self.bankroll)}.\n", WARNING, bold=True))
            elif self.bankroll <= 0:
                sys.stdout.write(color_text(f"{EMOJI_FAILURE} Balance depleted. Game over.\n", FAILURE, bold=True))
                return False
            else:
                self.current_bet = next_bet
                sys.stdout.write(color_text(f"{EMOJI_FAILURE} You lost! Bet doubled to {self.format_number(self.current_bet)}.\n", FAILURE, bold=True))

        # Append the new bankroll value to the history for charting
        self.bankroll_history.append(self.bankroll)
        return True

    def display_history(self):
        """
        Displays the detailed history of all bets, including results, bets, deltas, and balance.
        """
        clear_console()
        if not self.history:
            sys.stdout.write(color_text(f"\n{EMOJI_INFO} Bet history is empty.\n\n", INFO, bold=True))
            return

        # Format and print the header
        sys.stdout.write(color_text(f"\n{EMOJI_HIST} === Bet History ===\n", HEADER, bold=True))
        no_width, result_width, bet_width, balance_width, delta_width = 4, 7, 12, 14, 10
        header = (
            f"{color_text('No', HEADER, bold=True):<{no_width}}| "
            f"{color_text('Result', HEADER, bold=True):<{result_width}}| "
            f"{color_text('Bet', HEADER, bold=True):<{bet_width}}| "
            f"{color_text('Delta', HEADER, bold=True):<{delta_width}}| "
            f"{color_text('Balance', HEADER, bold=True):<{balance_width}}\n"
        )
        sys.stdout.write(header)
        sys.stdout.write(color_text("-" * (no_width + result_width + bet_width + delta_width + balance_width + 13) + "\n", INFO))

        # Print each entry in the history
        for i, (outcome, bet, delta, bankroll) in enumerate(self.history, 1):
            outcome_colored = color_text(f"{EMOJI_SUCCESS} W" if outcome == 'W' else f"{EMOJI_FAILURE} L", SUCCESS if outcome == 'W' else FAILURE)
            delta_colored = color_text(f"+{self.format_number(delta)}", SUCCESS) if delta > 0 else color_text(f"{self.format_number(delta)}", FAILURE)
            line = (
                f"{i:<{no_width}}| "
                f"{outcome_colored:<{result_width}}| "
                f"{color_text(self.format_number(bet), BET_BALANCE):<{bet_width}}| "
                f"{delta_colored:<{delta_width}}| "
                f"{color_text(self.format_number(bankroll), BET_BALANCE):<{balance_width}}\n"
            )
            sys.stdout.write(line)

        sys.stdout.write(color_text("=" * (no_width + result_width + bet_width + delta_width + balance_width + 13) + "\n\n", INFO))

    def display_statistics(self):
        """
        Displays summary statistics of the game, including total bets, wins/losses, ROI, and balance.
        """
        clear_console()
        total_bets = self.total_wins + self.total_losses
        roi = ((self.bankroll - self.bankroll_initial) / self.total_bet_amount) * 100 if self.total_bet_amount else 0
        roi_formatted = color_text(f"+{roi:.2f}%", SUCCESS) if roi > 0 else color_text(f"{roi:.2f}%", FAILURE)

        sys.stdout.write(color_text(f"\n{EMOJI_STATS} === Statistics ===\n", HEADER, bold=True))
        sys.stdout.write(color_text(f"{EMOJI_BANKROLL} Total bets: {total_bets}\n", WHITE))
        sys.stdout.write(color_text(f"{EMOJI_SUCCESS} Wins: {self.total_wins}\n", SUCCESS))
        sys.stdout.write(color_text(f"{EMOJI_FAILURE} Losses: {self.total_losses}\n", FAILURE))
        sys.stdout.write(color_text(f"{EMOJI_BET} Total bet amount: {self.format_number(self.total_bet_amount)}\n", BET_BALANCE))
        sys.stdout.write(color_text(f"{EMOJI_INFO} ROI (Return on Investment): {roi_formatted}\n", INFO))
        sys.stdout.write(color_text(f"{EMOJI_BANKROLL} Balance: {self.format_number(self.bankroll)}\n", BET_BALANCE))
        sys.stdout.write(color_text("====================\n\n", INFO))

    def display_chart(self):
        """
        Displays a chart of bankroll changes over time as a bar graph.
        """
        clear_console()
        if len(self.bankroll_history) < 2:
            sys.stdout.write(color_text(f"\n{EMOJI_INFO} Not enough data for the chart.\n\n", INFO, bold=True))
            return

        sys.stdout.write(color_text(f"\n{EMOJI_CHART} === Bankroll Chart ===\n", HEADER, bold=True))
        max_bankroll = max(self.bankroll_history)
        min_bankroll = min(self.bankroll_history)
        range_bankroll = max_bankroll - min_bankroll or 1
        chart_width = 50
        step = range_bankroll / chart_width

        sys.stdout.write(color_text(f"Initial bankroll: {self.format_number(self.bankroll_initial)}\n", INFO))
        sys.stdout.write(color_text(f"Max bankroll: {self.format_number(max_bankroll)}\n", SUCCESS))
        sys.stdout.write(color_text(f"Min bankroll: {self.format_number(min_bankroll)}\n", FAILURE))
        sys.stdout.write(color_text("-" * (chart_width + 15) + "\n", INFO))

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
        """
        Formats numbers for consistent and readable output (e.g., "1 000.00").
        """
        return f"{value:,.2f}".replace(",", " ")

def get_positive_float(prompt):
    """
    Prompts the user for a positive float value. Retries on invalid input.
    """
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
    """
    Displays the main program header.
    """
    header_text = "Martingale Strategy for European Roulette"
    sys.stdout.write(color_text(header_text + "\n\n", HEADER, bold=True))

def display_controls():
    """
    Displays available user controls.
    """
    sys.stdout.write(color_text(f"{EMOJI_SUCCESS} Enter 'w' (Win)\n", SUCCESS))
    sys.stdout.write(color_text(f"{EMOJI_FAILURE} Enter 'l' (Loss)\n", FAILURE))
    sys.stdout.write(color_text(f"{EMOJI_HIST} Enter 'h' (History)\n", INFO))
    sys.stdout.write(color_text(f"{EMOJI_STATS} Enter 's' (Statistics)\n", BET_BALANCE))
    sys.stdout.write(color_text(f"{EMOJI_CHART} Enter 'c' (Chart)\n", WARNING))
    sys.stdout.write(color_text(f"{EMOJI_EXIT} Enter 'e' (Exit)\n\n", WHITE))

def main():
    """
    Main program loop for user interaction.
    """
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
            bettor.display_history()
            input(color_text("Press Enter to continue...", INFO))
        elif outcome == 's':
            bettor.display_statistics()
            input(color_text("Press Enter to continue...", INFO))
        elif outcome == 'c':
            bettor.display_chart()
            input(color_text("Press Enter to continue...", INFO))
        elif outcome in ['w', 'l']:
            clear_console()  # Ensure the screen is refreshed after update
            bettor.update(outcome)
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