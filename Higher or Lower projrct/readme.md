# Higher Lower – Followers Guessing Game

This is a simple Python console game inspired by the **“Higher Lower”** follower-count game.  
You are shown two social media accounts and must guess which one has **more followers**.

---

##  Objective

Correctly guess whether **Account A** or **Account B** has more followers.  
Each correct guess increases your score by **1**. The game ends when you make a wrong guess.

---

##  How It Works

- The game randomly selects two different accounts from `game_data.data`.
- For each round:
  - Account A and Account B are displayed with their **name, description, and country**.
  - You type `A` or `B` based on who you think has more followers.
  - Your answer is checked against the follower counts stored in the data.
  - If you’re correct:
    - Your score increases.
    - Account B becomes the new Account A, and a new Account B is generated.
  - If you’re wrong:
    - The game prints your **final score** and exits.

---

##  Project Structure

- `main.py` (this script) – contains the main game loop and logic.
- `art.py` – contains the ASCII art variables:
  - `logo`
  - `vs`
- `game_data.py` – contains a list named `data` with account information:
  - `name`
  - `description`
  - `country`
  - `follower_count`

---

##  Requirements

- Python 3.x installed.

No external libraries are required; only the built-in `random` module is used.

---

##  How to Run

1. Make sure the following files are in the **same folder**:
   - `main.py` (your game file)
   - `art.py`
   - `game_data.py`
2. Open a terminal / command prompt in that folder.
3. Run:

   ```bash
   python main.py
