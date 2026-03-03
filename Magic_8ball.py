"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""

# Humza Bangash Magic8ball.py

import random

# TODO: Create a tuple of at least 8 responses
RESPONSES = ("Yes", "No", "Maybe", "Ask again later", "Without a doubt", "Very unlikely", "It is certain", "Better not tell you now")

print("Welcome to the Digital Oracle!")

# Keep the game running until the user quits
while True:
    question = input("Ask a yes/no question (or type 'quit' to exit): ").strip()

    # Exit condition
    if "quit" in question.lower():
        print("The Oracle bids you farewell.")
        break

    # Input validation: cannot be blank
    if question == "":
        print("❌ You must ask a question.")
        continue

    # Input validation: must end with a question mark
    if not question.endswith("?"):
        print("❌ That doesn't look like a question. Try again.")
        continue

    # Valid question → give response
    print("🔮", random.choice(RESPONSES))


