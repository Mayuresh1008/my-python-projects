import random

word_list = ["aardvark", "baboon", "camel"]

# assigining variable to the random word
chosen_word = random.choice(word_list)

print(chosen_word)

# assigning variable to the guessed letter

guess = input("Guess a letter: ").lower()

# Checking does the guessed letter present in the chosen word

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
