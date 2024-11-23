# 🎲 Betulator - Martingale Strategy Tracker for European Roulette

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
4. [Why Martingale?](#-why-the-martingale-strategy)
5. [How the Martingale Strategy Works](#-how-does-the-martingale-strategy-work)
6. [Probability and Risks](#-probability-and-risks)
7. [Financial Implications](#-financial-implications)
8. [Casino Constraints](#-casino-constraints)
9. [Advanced Concepts](#-advanced-concepts)
10. [Customization](#-customization)
11. [FAQs](#-faqs)
12. [License](#-license)
13. [Feedback and Contributions](#-feedback-and-contributions)

---

## 🎯 What Is This Tool?

The **Martingale Strategy Tracker** is a **bet-tracking and analysis tool** for live European roulette.  
It is designed to:
- **Track your bets in real-time**:
  - Automatically calculates your next bet size based on the Martingale progression.
  - Keeps an organized record of wins, losses, and bankroll changes.
- **Visualize your performance**:
  - Displays detailed statistics and summaries.
- **Analyze your strategy**:
  - Provides ROI, win/loss ratios, and detailed history.

---

## 🛠️ Installation

### ✅ Supported Platforms

1. **Windows**:  
   Works flawlessly on Command Prompt, PowerShell, or Windows Terminal.
2. **macOS/Linux**:  
   Compatible with any standard terminal application.

### 🛠️ Installation Steps

1. **Install Python 3.6+**  
   Download Python from the [official website](https://www.python.org/).

2. **Clone the Repository**  
   Open your terminal and execute:
   ```bash
   git clone https://github.com/NetBr3ak/betulator.git
   cd betulator
   ```

3. **Install Dependencies**  
   Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Program**  
   Start the tool by typing:
   ```bash
   python main.py
   ```

---

## 🎮 How to Use

### Step 1: Launch the Tool
Run the program using `python main.py`. Input your **initial bet size** and **starting bankroll**.

### Step 2: Play Roulette
Input the outcome of each round:
- **`w`**: Record a win.
- **`l`**: Record a loss.

### Step 3: Explore Features
Use the following commands during your session:
- **`h`**: View detailed bet history.
- **`s`**: Check statistics.
- **`e`**: Exit the program.

---

## 🤔 Why the Martingale Strategy?

The **Martingale strategy** is enticing due to its simplicity and its promise:
1. **Guaranteed recovery**: After every win, all previous losses are erased, and you achieve a profit equal to the initial bet \( b \).
2. **Ease of execution**: Double your bet after each loss, reset to the initial bet after each win.

However, beneath this simplicity lies the harsh reality of exponential growth, finite bankrolls, and the casino's edge. Let's delve into the mathematics and practical implications of Martingale.

---

## 🧠 How Does the Martingale Strategy Work?

### Key Rules
- **Double your bet** after every loss.
- **Reset to the initial bet** (`b`) after every win.

### Core Equations

#### Next Bet After L Losses
The bet size after `L` losses:
```
b_next = b * 2^L
```

#### Total Amount Wagered After L Losses
The cumulative amount wagered:
```
W_total = b * (2^L - 1)
```

#### Profit After a Win
Guaranteed profit after a win:
```
Profit = b
```

### Example: Bet Progression
If the initial bet is `b = 10` and you lose 3 times in a row:
- First bet: `b = 10`
- Second bet: `b = 10 * 2 = 20`
- Third bet: `b = 20 * 2 = 40`
- Fourth bet: `b = 40 * 2 = 80`

The total amount wagered:
```
W_total = 10 + 20 + 40 + 80 = 150
```

The profit if you win the fourth bet:
```
Profit = 10
```

## 📊 Probability and Risks

### Roulette Probabilities
In European roulette:
- **Winning Probability**:
```
P(win) = 18 / 37 ≈ 48.65%
```

- **Losing Probability**:
```
P(lose) = 19 / 37 ≈ 51.35%
```

### Losing Streak Probability
The probability of losing `L` consecutive bets:
```
P(loss_streak) = (19 / 37)^L
```

#### Example Calculations:
- Probability of losing 3 times in a row:
  ```
  P(loss_streak, 3) = (19 / 37)^3 ≈ 13.96%
  ```

- Probability of losing 5 times in a row:
  ```
  P(loss_streak, 5) = (19 / 37)^5 ≈ 2.18%
  ```

- Probability of losing 10 times in a row:
  ```
  P(loss_streak, 10) = (19 / 37)^10 ≈ 0.048%
  ```

## 🧮 Financial Implications

### Exponential Growth of Bets
The size of bets grows exponentially after consecutive losses:
```
b_next = b * 2^L
```

#### Example:
- Initial bet: `b = 10`
- After 5 losses:
  ```
  b_next = 10 * 2^5 = 320
  ```
- After 10 losses:
  ```
  b_next = 10 * 2^10 = 10,240
  ```

### Total Amount Wagered
The total amount wagered after `L` losses:
```
W_total = b * (2^L - 1)
```

#### Example:
- `b = 10`, `L = 10`:
  ```
  W_total = 10 * (2^10 - 1) = 10,230
  ```

## 🏦 Casino Constraints

### Table Limits
Most casinos impose limits to prevent Martingale abuse. For example:
- **Minimum Bet**: `b_min = 10`
- **Maximum Bet**: `b_max = 500`

The maximum streak you can sustain before hitting the limit:
```
L_max = log2(b_max / b_min)
```

#### Example:
- `b_min = 10`, `b_max = 500`:
  ```
  L_max = log2(500 / 10) = 5.64
  ```
Thus, you can only double up 5 times before exceeding the table limit.

## 🔢 Advanced Concepts

### Risk of Ruin
The **Risk of Ruin** measures the probability of losing your entire bankroll before achieving a win:
```
Risk of Ruin = (1 - e)^(B / b)
```
Where:
- `B` is the bankroll,
- `b` is the initial bet,
- `e` is the house edge (`e = 0.027` for European roulette).

#### Example:
- `B = 1,000`, `b = 10`:
  ```
  Risk of Ruin = (1 - 0.027)^(1000 / 10) ≈ 5.04%
  ```

### Expected Value (EV)
The **Expected Value** combines probabilities and outcomes:
```
EV = P(win) * Profit - P(lose) * Loss
```

#### Example:
- `b = 10`,
- `P(win) = 48.65%`,
- `P(lose) = 51.35%`,
- Total loss after 5 streaks `W_total = 310`:
  ```
  EV = (0.4865 * 10) - (0.5135 * 310) ≈ -5.31
  ```

The negative `EV` confirms that the house edge ensures a long-term loss.

## 📊 Summary Table

| Metric                      | Formula                     | Example (`b = 10`, `L = 5`) |
|-----------------------------|-----------------------------|-----------------------------|
| Next Bet Size               | `b_next = b * 2^L`         | `b_next = 320`             |
| Total Wagered               | `W_total = b * (2^L - 1)`  | `W_total = 310`            |
| Probability of Losing Streak| `P(loss_streak) = (19/37)^L`| `P = 2.18%`                |
| Risk of Ruin                | `(1 - e)^(B / b)`          | `Risk = 5.04%`             |

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
