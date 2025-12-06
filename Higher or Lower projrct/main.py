# Display art
from art import logo, vs
from game_data import data
import random

print(logo)
score = 0
game_should_continue = True

# start with one random account for B
account_b = random.choice(data)

while game_should_continue:
    # move B to A, pick a new B
    account_a = account_b
    account_b = random.choice(data)
    while account_b == account_a:  # ensure different accounts
        account_b = random.choice(data)

    # inline format_data
    a_display = f"{account_a['name']}, a {account_a['description']}, from {account_a['country']}"
    b_display = f"{account_b['name']}, a {account_b['description']}, from {account_b['country']}"

    print(f"Compare A: {a_display}.")
    print(vs)
    print(f"Against B: {b_display}.")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").strip().lower()

    # Clear the screen
    print("\n" * 20)
    print(logo)

    # Get follower counts (inline check_answer logic will use these)
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # inline check_answer logic
    if a_follower_count > b_follower_count:
        is_correct = (guess == "a")
    else:
        is_correct = (guess == "b")

    # Give user feedback and update score
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False
