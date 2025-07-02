"""
This is basic number guessing game
In this game i have used concepts like whileloop, random, if-else and input() function
"""

import random

is_correct = False
attempts = 0

correct_number = random.randint(1, 100)

print("--------------- NUMBER GUESSING GAME ---------------")

while not is_correct:

    guess = int(input("Enter a guess:"))
    attempts += 1
    if guess > correct_number:
        print("Too High!!")
    elif guess < correct_number:
        print("Too Low!!")
    else:
        print(f"Yay!, Your guess is correct number in {attempts} attempts.")
        is_correct = True
