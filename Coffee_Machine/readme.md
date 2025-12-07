ChatGPT said:
# ☕ Coffee Machine – Python Console Program

This is a simple **coffee machine simulator** written in Python.  
It lets a user order drinks (espresso, latte, cappuccino), pays with virtual coins, and tracks resources and profit.

---

##  Features

- Three drink options:
  - `espresso`
  - `latte`
  - `cappuccino`
- Checks if there are enough **resources** (water, milk, coffee) before making a drink.
- Accepts “coins”:
  - quarters, dimes, nickles, pennies
- Calculates:
  - total money inserted
  - change to return to the user
- Tracks:
  - remaining ingredients
  - total profit made
- Special commands:
  - `report` → shows current resources and money
  - `off` → turns off the machine (ends the program)

---

##  Program Logic Overview

### 1. `MENU`
A dictionary that stores each drink’s:
- required `ingredients`
- `cost`

```python
MENU = {
    "espresso": { ... },
    "latte": { ... },
    "cappuccino": { ... }
}

2. resources

Tracks how much water, milk, and coffee the machine currently has.

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

3. Main Functions

is_resource_sufficient(order_ingredients)
Checks if there is enough water/milk/coffee to make the selected drink.

process_coins()
Asks the user how many coins they are inserting and returns the total amount of money.

is_transaction_successful(money_received, drink_cost)

Verifies if enough money was inserted.

Prints change, updates profit, and returns True if successful.

Refunds money and returns False otherwise.

make_coffee(drink_name, order_ingredients)
Deducts the used ingredients from resources and prints a message serving the drink.

 Main Loop

The program runs in a while is_on: loop:

Asks:

What would you like? (espresso/latte/cappuccino):


Handles commands:

off → stop the machine

report → print resources and profit

drink name (espresso, latte, cappuccino) → proceed to:

check resources

process coins

check transaction

make coffee

 How to Run

Save the code in a file, e.g. main.py.

Make sure Python 3 is installed.

Open a terminal in the project folder.

Run:

python main.py


Follow the prompts in the console:

Type a drink name: espresso, latte, or cappuccino

Insert coins when asked

Use report to see current status

Use off to exit
