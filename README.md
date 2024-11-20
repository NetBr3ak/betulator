### 🎲 Betulator - Martingale Strategy Tracker for European Roulette

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**"Gambling is a tax on people who are bad at math."**

But what if you’re **good** at math? Welcome to the **Martingale Strategy Tracker**—a tool designed to help you meticulously apply and monitor the **Martingale Strategy** in live European roulette.

If you’ve ever thought *"The house edge can’t defeat me if I double my bets!"*, this tracker is your companion. But remember: **Martingale is simple in concept, but risky in practice**.

Let’s dive into the **theory, math, and humor** behind one of the most famous (and flawed) betting systems in gambling history.

---

## 📜 Table of Contents

1. [What Is This Tool?](#-what-is-this-tool)
2. [Installation](#-installation)
3. [How to Use](#-how-to-use)
4. [Key Features](#-key-features)
5. [Why Martingale?](#-why-the-martingale-strategy)
6. [How the Martingale Strategy Works](#-how-does-the-martingale-strategy-work)
7. [Probability and Risks](#-probability-and-risks)
8. [Financial Implications](#-financial-implications)
9. [Casino Constraints](#-casino-constraints)
10. [Advanced Concepts](#-advanced-concepts)
11. [Customization](#-customization)
12. [FAQs](#-faqs)
13. [License](#-license)
14. [Feedback and Contributions](#-feedback-and-contributions)

---

## 🎯 What Is This Tool?

The **Martingale Strategy Tracker** is a **bet-tracking and analysis tool** for live European roulette.  
It is designed to:
- **Track your bets in real-time**:
  - Automatically calculates your next bet size based on the Martingale progression.
  - Keeps an organized record of wins, losses, and bankroll changes.
- **Visualize your performance**:
  - Generates intuitive charts to display the rise and fall of your bankroll.
- **Analyze your strategy**:
  - Provides detailed statistics, such as ROI, win/loss ratios, and total wagers.

If the Martingale strategy is your sword, this tool is your scabbard, sharpening and organizing your approach.

---

## 🛠️ Installation

### ✅ Supported Platforms

1. **Windows**:  
   Works flawlessly on Command Prompt, PowerShell, or Windows Terminal.
2. **macOS/Linux**:  
   Compatible with any standard terminal application.
3. **Android (Alpha testing)**:  
   Run it on the go using [Termux](https://termux.dev/) or similar terminal emulators.

### 🛠️ Installation Steps

1. **Install Python 3.6+**  
   - Download Python from the [official website](https://www.python.org/).
   - Ensure `python` and `pip` are available in your terminal.

2. **Clone the Repository**  
   Open your terminal and execute:
   ```bash
   git clone https://github.com/NetBr3ak/betulator.git
   cd betulator
   ```

3. **Run the Program**  
   Start the tool by typing:
   ```bash
   python betulator.py
   ```

4. **Follow Prompts**  
   Enter your **initial bet** and **starting bankroll** to begin tracking your roulette gameplay.

### 📷 Visual Demonstrations

#### Example on Windows Terminal
<img src="images/windows_terminal_example.png" alt="Windows Terminal Example" width="800">

#### Example on Android (Termux)
<img src="images/termux_terminal_example.png" alt="Termux Example" width="300">

---

## 🎮 How to Use

### Step 1: Launch the Tool
Run the program using the command above. You’ll be greeted with prompts to enter your **initial bet size** and **starting bankroll**.

### Step 2: Play Roulette
Input the outcome of each round:
- **`w`**: Record a win.
- **`l`**: Record a loss.

### Step 3: View Progress
Use these commands during your session:
- **`h`**: View detailed bet history.
- **`s`**: Check your statistics.
- **`c`**: See a visual chart of your bankroll over time.
- **`e`**: Exit the program.

---

## 🌟 Key Features

### 1. 📜 Bet History
Keep track of every bet you place:
- Round number.
- Bet size.
- Result (win or loss).
- Balance change (delta).
- Current bankroll.

Example output:
```bash
📜 === Bet History ===
No   | Result | Bet    | Delta  | Balance
--------------------------------------------
1    | ✅ W   | 10.00  | +10.00 | 1010.00
2    | ❌ L   | 10.00  | -10.00 | 1000.00
3    | ❌ L   | 20.00  | -20.00 |  980.00
4    | ✅ W   | 40.00  | +40.00 | 1020.00
```

### 2. 📊 Detailed Statistics
Analyze your performance with aggregated metrics:
- **Total bets placed**.
- **Win/loss record**.
- **ROI (Return on Investment)**.
- **Net profit/loss**.

Example:
```bash
📊 === Statistics ===
💰 Total bets: 4
✅ Wins: 2
❌ Losses: 2
🎲 Total bet amount: 80.00
📘 ROI (Return on Investment): +20.00%
💰 Balance: 1020.00
```

### 3. 📈 Bankroll Chart
Visualize the trajectory of your bankroll. A bar chart plots your balance after each round, making it easy to identify trends.  
Example:
```bash
📈 === Bankroll Chart ===
Initial bankroll: 1000.00
Max bankroll: 1020.00
Min bankroll: 980.00
---------------------------------------------
  1000.00 | ███████
   980.00 | ████
  1020.00 | █████████████
---------------------------------------------
```

---

## 🤔 Why the Martingale Strategy?

The **Martingale strategy** is enticing due to its simplicity and its promise:
1. **Guaranteed recovery**: After every win, all previous losses are erased, and you achieve a profit equal to the initial bet \( b \).
2. **Ease of execution**: Double your bet after each loss, reset to the initial bet after each win.

However, beneath this simplicity lies the harsh reality of exponential growth, finite bankrolls, and the casino's edge. Let's delve into the mathematics and practical implications of Martingale.

---

## 🧠 How Does the Martingale Strategy Work?

### Key Rules
1. **Double your bet** after every loss.
2. **Reset to the initial bet** \( b \) after every win.

### Core Equations

#### Next Bet After \( L \) Losses
The bet size after \( L \) losses:
$$
b_{\text{next}} = b \cdot 2^L
$$

#### Total Amount Wagered After \( L \) Losses
The cumulative amount wagered:
$$
W_{\text{total}} = b \cdot (2^L - 1)
$$

#### Profit After a Win
Guaranteed profit after a win:
$$
\text{Profit} = b
$$

### Example: Bet Progression
If the initial bet is \( b = 10 \) and you lose 3 times in a row:
- First bet: \( b = 10 \)
- Second bet: \( b = 10 \cdot 2 = 20 \)
- Third bet: \( b = 20 \cdot 2 = 40 \)
- Fourth bet: \( b = 40 \cdot 2 = 80 \)

The total amount wagered:
$$
W_{\text{total}} = 10 + 20 + 40 + 80 = 150
$$

The profit if you win the fourth bet:
$$
\text{Profit} = 10
$$

---

## 📊 Probability and Risks

### Roulette Probabilities
In European roulette:
- **Winning Probability**:
$$
P(\text{win}) = \frac{18}{37} \approx 48.65\%
$$

- **Losing Probability**:
$$
P(\text{lose}) = \frac{19}{37} \approx 51.35\%
$$

### Losing Streak Probability
The probability of losing \( L \) consecutive bets:
$$
P(\text{loss streak}) = \left( \frac{19}{37} \right)^L
$$

#### Example Calculations:
- Probability of losing 3 times in a row:
  $$
  P(\text{loss streak, 3}) = \left( \frac{19}{37} \right)^3 \approx 13.96\%
  $$

- Probability of losing 5 times in a row:
  $$
  P(\text{loss streak, 5}) = \left( \frac{19}{37} \right)^5 \approx 2.18\%
  $$

- Probability of losing 10 times in a row:
  $$
  P(\text{loss streak, 10}) = \left( \frac{19}{37} \right)^{10} \approx 0.048\%
  $$

---

## 🧮 Financial Implications

### Exponential Growth of Bets
The size of bets grows exponentially after consecutive losses:
$$
b_{\text{next}} = b \cdot 2^L
$$

#### Example:
- Initial bet: \( b = 10 \)
- After 5 losses:
  $$
  b_{\text{next}} = 10 \cdot 2^5 = 320
  $$
- After 10 losses:
  $$
  b_{\text{next}} = 10 \cdot 2^{10} = 10,240
  $$

### Total Amount Wagered
The total amount wagered after \( L \) losses:
$$
W_{\text{total}} = b \cdot (2^L - 1)
$$

#### Example:
- \( b = 10 \), \( L = 10 \):
  $$
  W_{\text{total}} = 10 \cdot (2^{10} - 1) = 10,230
  $$

---

## 🏦 Casino Constraints

### Table Limits
Most casinos impose limits to prevent Martingale abuse. For example:
- **Minimum Bet**: \( b_{\text{min}} = 10 \)
- **Maximum Bet**: \( b_{\text{max}} = 500 \)

The maximum streak you can sustain before hitting the limit:
$$
L_{\text{max}} = \log_2\left(\frac{b_{\text{max}}}{b_{\text{min}}}\right)
$$

#### Example:
- \( b_{\text{min}} = 10 \), \( b_{\text{max}} = 500 \):
  $$
  L_{\text{max}} = \log_2\left(\frac{500}{10}\right) = 5.64
  $$
Thus, you can only double up 5 times before exceeding the table limit.

---

## 🔢 Advanced Concepts

### Risk of Ruin
The **Risk of Ruin** measures the probability of losing your entire bankroll before achieving a win:
$$
\text{Risk of Ruin} = (1 - e)^{\frac{B}{b}}
$$
Where:
- \( B \) is the bankroll,
- \( b \) is the initial bet,
- \( e \) is the house edge (\( e = 0.027 \) for European roulette).

#### Example:
- \( B = 1,000 \), \( b = 10 \):
  $$
  \text{Risk of Ruin} = (1 - 0.027)^{\frac{1000}{10}} \approx 5.04\%
  $$

### Expected Value (EV)
The **Expected Value** combines probabilities and outcomes:
$$
EV = P(\text{win}) \cdot \text{Profit} - P(\text{lose}) \cdot \text{Loss}
$$

#### Example:
- \( b = 10 \),
- \( P(\text{win}) = 48.65\% \),
- \( P(\text{lose}) = 51.35\% \),
- Total loss after 5 streaks \( W_{\text{total}} = 310 \):
  $$
  EV = (0.4865 \cdot 10) - (0.5135 \cdot 310) \approx -5.31
  $$

The negative \( EV \) confirms that the house edge ensures a long-term loss.

---

## 📊 Summary Table

| Metric                      | Formula                          | Example (\( b = 10 \), \( L = 5 \))        |
|-----------------------------|----------------------------------|--------------------------------|
| Next Bet Size               | \( b_{\text{next}} = b \cdot 2^L \)  | \( b_{\text{next}} = 320 \)        |
| Total Wagered               | \( W_{\text{total}} = b \cdot (2^L - 1) \) | \( W_{\text{total}} = 310 \)       |
| Probability of Losing Streak| \( P(\text{loss streak}) = (19 / 37)^L \) | \( P = 2.18\% \)                   |
| Risk of Ruin                | \( (1 - e)^{B/b} \)                 | \( \text{Risk} = 5.04\% \)         |

---

## ⚠️ Conclusion

The **Martingale strategy** is alluring in its simplicity but flawed in execution. The exponential growth of bets, combined with finite bankrolls and casino-imposed limits, ensures its unsustainability.

Despite its short-term appeal, Martingale remains a cautionary tale of how mathematics governs chance. 🎲

## 🔧 Customization

Feel like tweaking the tool? You can:
1. **Experiment with Alternative Strategies**:
   - Fibonacci: A safer progression that increases bets more gradually.
   - Kelly Criterion: Bet proportionally based on your perceived edge.
2. **Add Realistic Constraints**:
   - Implement table limits.
   - Adjust starting bankrolls and bet increments.
3. **Extend Features**:
   - Simulate thousands of rounds to analyze long-term outcomes.

---

## 💬 FAQs

### Q1: Can Martingale guarantee a profit?
No. While the strategy can deliver **short-term wins**, it collapses under prolonged losing streaks or table limits.

### Q2: Is this tool a simulator?
No. This tool tracks your bets and progress during live games. It does not simulate spins or predict outcomes.

### Q3: Can I use this tool for other games?
Yes! The principles apply to any game with binary outcomes, such as coin flips or blackjack side bets.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). Feel free to modify, share, and use responsibly.

---

## 💬 Feedback and Contributions

Have ideas to make this tool even better? Found a bug? Open an issue or submit a pull request.

And remember: **"In gambling, math is your friend—but only if you know when to quit."**

---
