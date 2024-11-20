# 🎲 Betulator 🎰  
_“The ultimate Martingale strategy simulator.”_

Betulator is a Python-based simulation tool that lets you explore the **Martingale betting strategy**, a popular progressive betting system. Whether you’re a mathematician, a curious gambler, or just someone fascinated by probability, this program allows you to test the mechanics of Martingale in a controlled, risk-free environment.  

---

## 🌟 **Features**  
- **Pure Python:** No external libraries required. Just Python, a terminal, and your curiosity.  
- **Cross-Platform:** Works on PCs 💻, Macs 🍏, Linux 🐧, and even mobile devices 📱 via terminal apps like Termux.  
- **Detailed Analytics:**  
  - **Bet History:** Track every win and loss with detailed logs.  
  - **Statistics:** View metrics like wins, losses, and ROI.  
  - **Bankroll Chart:** Watch your bankroll evolve over time with clear ASCII visualizations.  
- **Interactive Gameplay:** Simulate rounds, make decisions, and explore outcomes.  
- **Educational Tool:** Learn how progressive betting strategies work and gain insights into probability and bankroll management.

---

## 🚀 **How to Use**

### 1. Clone the Repo
bash
git clone https://github.com/YourUsername/Betulator.git
cd Betulator

### 2. Run the Program
bash
python betulator.py

### 3. Explore the Simulation
- Enter your starting bankroll and initial bet.
- Simulate rounds:
  - `w` for **Win** 🤑  
  - `l` for **Loss** 💸  
  - `h` for **History** 📜  
  - `s` for **Statistics** 📊  
  - `c` for **Chart** 📈  
  - `e` to **Exit** 🚪  

The program will handle all calculations, leaving you to focus on the strategy.

---

## 📸 **Screenshots**

- **Desktop View**  
  _Detailed stats and colorful results, optimized for larger terminals._  
  ![Desktop Screenshot](path/to/desktop-screenshot.png)

- **Mobile View**  
  _Perfect for on-the-go exploration, fully compatible with mobile terminals._  
  ![Mobile Screenshot](path/to/mobile-screenshot.png)

---

## 🛠️ **How Betulator Works**

### **The Martingale Strategy**  
The Martingale betting system is based on doubling your bet after every loss. The goal is to recover all previous losses and achieve a net profit equal to your initial bet when you eventually win.

### **How It Works:**  
1. Start with an initial bet (e.g., $10).  
2. If you lose, double your bet for the next round.  
3. When you win, reset your bet to the initial amount and pocket a profit equal to your starting bet.  
4. Repeat the process for as many rounds as you’d like.  

### **Example:**
- Initial bet: $10  
- Sequence: Lose ($10), Lose ($20), Lose ($40), Win ($80)  
- Total wagered: $10 + $20 + $40 + $80 = $150  
- Total winnings: $80  
- Net profit: $80 - $150 + $80 = $10 (equal to your starting bet).

This makes Martingale attractive for games with close to 50/50 odds, such as roulette.

---

## 🌍 **Why Betulator?**

1. **Risk-Free Exploration:** Simulate the Martingale strategy without risking real money.  
2. **Learn by Doing:** Test how the strategy holds up under different conditions and streaks of losses.  
3. **Track Results:** View detailed stats and graphs of your bankroll progression.  
4. **Portable:** Run it on your desktop or mobile device, anywhere Python works.  

---

## 📊 **Visual Insights**

- **Bet History:** A detailed log of every round, including the outcome, bet amount, and remaining bankroll.  
- **Bankroll Chart:** An ASCII visualization of your bankroll over time.  
- **Statistics Dashboard:** A summary of wins, losses, and overall performance.

---

## 📜 **License**

This project is licensed under the MIT License. You’re free to use, modify, and share it.

---

## ⚠️ **Disclaimer**

The Martingale strategy is a progressive betting system that assumes unlimited funds and no table limits to ensure success. In real-world scenarios, these assumptions rarely hold, and prolonged use can lead to significant losses. Use this simulator to understand the mechanics and risks, but always gamble responsibly.
