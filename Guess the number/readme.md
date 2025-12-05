## Number Guessing Game (Python):

A fun and interactive command-line game where the player tries to guess a randomly selected number between 1 and 100.
The game includes two difficulty levels and gives feedback on each guess until the player wins or runs out of attempts.

## Features:

Random number generation (1–100)

##Two difficulty modes:

Easy → 10 attempts

Hard → 5 attempts

Feedback on guesses:

Too high

Too low

Attempt tracking

Simple, beginner-friendly code structure

## Concepts Practiced:

Functions in Python

While loops and control flow

Global vs local variables

Return values

Random number generation (randint)

User input handling

## How It Works

The game selects a random number between 1 and 100

You choose a difficulty:

easy → 10 attempts

hard → 5 attempts

You guess numbers until:

You find the correct answer 🎉

OR you run out of attempts ❌

After each guess, you get hints:

Too high

Too low

## How to Run

Inside the project folder, run:

python main.py


Make sure you have the required art.py file or ASCII logo imported in the script.

📁 File Structure (Recommended)
number_guessing_game/
│── main.py
│── art.py
│── README.md

## Sample Output
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
Make a guess: 45
Too high.
Guess again.
