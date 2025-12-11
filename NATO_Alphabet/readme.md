## Project Overview

This program:

Loads the NATO Phonetic Alphabet from a CSV file

Creates a dictionary mapping each letter to its NATO code word

Takes a word from the user

Converts the word into a list of phonetic code words

Prints the final code word list

Example:
Input → "HELLO"
Output → ['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']

📂 Files in This Project
├── nato_phonetic_alphabet.csv
├── main.py
└── README.md


nato_phonetic_alphabet.csv contains two columns:

letter

code

## How the Code Works
1️⃣ Import pandas
import pandas

2️⃣ Read the CSV file
data = pandas.read_csv("nato_phonetic_alphabet.csv")

3️⃣ Create a dictionary using dictionary comprehension
dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

4️⃣ Get user input and convert it to uppercase
word = input("Enter a word: ").upper()

5️⃣ Convert each letter into its phonetic code word
output = [dictionary[letter] for letter in word]
print(output)

## Sample Output
Enter a word: anirudh
['Alfa', 'November', 'India', 'Romeo', 'Uniform', 'Delta', 'Hotel']

## Error Handling (Optional Improvement)

If the user enters something that isn’t a letter (like a number), the program will break.

You can add this in the future:

try:
    output = [dictionary[letter] for letter in word]
except KeyError:
    print("Sorry, only letters please.")

## Concepts Covered

Reading CSV files with pandas

Dictionary comprehension

Iterating through DataFrames using .iterrows()

User input handling

List comprehension

🏁 Final Thoughts

This mini-project is a great introduction to using pandas for data processing and practicing dictionary & list comprehensions. It also reinforces clean input → process → output workflow.
