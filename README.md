# 🎲 Martingale Strategy Tracker for European Roulette - Betulator

**"Luck is what happens when preparation meets opportunity." — Seneca**  
But in gambling, it often feels more like **"Luck is what happens when math takes your wallet hostage."** Welcome to the **Martingale Strategy Tracker**, a scientifically engineered (and mildly sarcastic) tool to help you apply and monitor the **Martingale betting strategy** in **European roulette**.

Whether you're here to challenge the odds, explore the limits of probability, or simply document your descent into financial chaos, this tool is your loyal companion. 

Let’s dive into the **math, logic, and hilarity** of trying to outwit a system built to keep you losing.

---

## 🎯 What Is This Tool?

This tool is not magic, nor does it claim to defy the laws of the universe. What it **does do**:
- **Tracks your bets in real-time**: Keeps you organized and ensures you stay on the Martingale path (no cheating!).
- **Provides detailed analytics**:
  - Historical records of bets, outcomes, and bankroll changes.
  - Key statistics, including ROI, win/loss ratios, and total wagers.
- **Visualizes your progress**:
  - Charts your bankroll as it rises... or plummets.
- **Keeps you accountable**:
  - Like an honest friend reminding you, "Doubling down might not end well."

---

## 🧠 The Science Behind Martingale

### 🎲 The Alluring Simplicity

The **Martingale strategy** is built on the premise of **doubling down until you win**, which guarantees:
1. Recovery of all previous losses.
2. A net profit equal to your initial bet.

Sounds foolproof, right? Not quite.

The **core assumption** is that a win is inevitable if you play long enough. But like all things in life—relationships, diets, and cryptocurrency investments—Martingale doesn't work as smoothly as advertised. 

Let’s break it down mathematically.

---

### 🧮 Mathematical Foundations

#### 1. Bet Progression
After `L` consecutive losses, the bet for the next round is:
bash
b_next = b * 2^L

#### 2. Total Wagered
The total amount wagered after `L` losses:
bash
total_wagered = b * (2^L - 1)

Example:
- Initial bet (`b`) = €10
- After 5 losses:
bash
total_wagered = 10 * (2^5 - 1) = €310

#### 3. Net Profit
If you win after `L` losses, the profit is always equal to the initial bet:
bash
profit = b

This is the **irresistible promise** of Martingale: no matter how deep you dig, one win brings you back to zero (and adds €10 on top).

---

### 📊 Probabilities: How Likely Are You to Lose?

#### 1. Winning Probability
In European roulette, there are 18 red and 18 black numbers, but the sneaky green zero tips the odds in favor of the house:
bash
P(win) = 18 / 37 ≈ 48.65%

#### 2. Losing Streak Probability
The probability of losing `L` consecutive bets:
bash
P(loss_streak) = (19 / 37)^L

Example:
- Probability of losing 5 times in a row:
bash
P(loss_streak_5) = (19 / 37)^5 ≈ 2.18%

This seems low... until you hit a streak of 10 losses. Then you're betting the price of a used car. 🚗

#### 3. Expected Loss
The **house edge** (2.7%) ensures that, over time, your losses will add up:
bash
Expected_loss = Total_wagered * House_edge

Example:
- Total wagered = €1,000
- Expected loss:
bash
Expected_loss = 1,000 * 0.027 = €27

This is why casinos love Martingale players: short-term thrills, long-term losses.

---

## 🤔 Why Martingale? Why Not Something Else?

### What I Considered:
1. **Fibonacci Strategy**  
   - A safer progression: bets follow the Fibonacci sequence (1, 1, 2, 3, 5...).
   - Slower loss accumulation, but also slower recovery.  
   **Verdict**: Too slow. Life’s short, and so is my patience.

2. **Kelly Criterion**  
   - Maximizes bankroll growth by betting a fraction proportional to your edge.  
   **Verdict**: Useless without an edge. In roulette, the house always has it.

3. **D'Alembert System**  
   - Increase your bet by 1 unit after a loss, decrease by 1 after a win.  
   **Verdict**: Safe, but painfully slow to recover losses.

### Why Martingale?
- **Immediate Recovery**: One win erases all losses.  
- **Psychological Appeal**: Feels like you’re always one step away from victory.  
- **The Fun Factor**: Exponential betting is exciting, in the same way skydiving without a parachute is.

---

## 📈 Advanced Insights into Risk and Reward

### Risk of Ruin
The probability of depleting your bankroll depends on:
- Starting balance (`B`)
- Initial bet (`b`)
- House edge (`e`)

The formula for **Risk of Ruin**:
bash
Risk_of_Ruin = (1 - e)^(B / b)

### When Does Martingale Break?

1. **Casino Table Limits**  
   Most casinos cap bets to prevent Martingale abuse. Example:
   - Table limit = €500
   - Starting bet = €10
   - You max out after 6 losses:
bash
b_next = 10 * 2^6 = €640 (not allowed)

2. **Bankroll Exhaustion**  
   Even without limits, exponential growth catches up. Starting with €1,000:
   - After 7 losses, you've wagered €1,270 total.

---

## 🎮 How to Use This Tool

1. **Run the Program**:
bash
python martingale_tracker.py

2. **Input Your Initial Bet and Bankroll**:
bash
🎲 Initial bet: 10
💰 Starting balance: 1000

3. **Play and Track Results**:
   - Enter `w` for a win, `l` for a loss.
   - Use commands:
     - `h`: View bet history.
     - `s`: Check statistics.
     - `c`: See bankroll chart.
     - `e`: Exit.

---

## 📊 Example Outputs

### Bet History
bash
📜 === Bet History ===
No   | Result | Bet    | Delta  | Balance
--------------------------------------------
1    | ✅ W   | 10.00  | +10.00 | 1010.00
2    | ❌ L   | 10.00  | -10.00 | 1000.00
3    | ❌ L   | 20.00  | -20.00 |  980.00
4    | ✅ W   | 40.00  | +40.00 | 1020.00

### Statistics
bash
📊 === Statistics ===
💰 Total bets: 4
✅ Wins: 2
❌ Losses: 2
🎲 Total bet amount: 80.00
📘 ROI (Return on Investment): +20.00%
💰 Balance: 1020.00

### Bankroll Chart
bash
📈 === Bankroll Chart ===
Initial bankroll: 1000.00
Max bankroll: 1020.00
Min bankroll: 980.00
---------------------------------------------
  1000.00 | ███████
   980.00 | ████
  1020.00 | █████████████
---------------------------------------------

---

## 🌍 Compatibility

Works seamlessly on:
- **Windows**: Command Prompt, PowerShell, or Windows Terminal.
- **macOS/Linux**: Any terminal.
- **Android**: Use Termux for on-the-go gambling management.

---

## 🔧 Customization

Want to tweak the tool? Modify it to:
- Experiment with different doubling factors.
- Add realistic bet limits.
- Simulate alternative strategies (Fibonacci, Labouchère, Kelly Criterion).

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). Share, modify, and use responsibly.

---

## 💬 Feedback

Have ideas for improvement? Found a bug? Submit an issue or a PR.  
Just remember: **Martingale doesn’t beat the house, but it sure makes losing entertaining.** 😉
