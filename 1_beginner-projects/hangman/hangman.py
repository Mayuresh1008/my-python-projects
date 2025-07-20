import random

word_list = ["aardvark", "baboon", "camel"]

# assigining variable to the random word
chosen_word = random.choice(word_list)

print(chosen_word)

# adding placeholder with same numbers of blanks as the chosen_word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print(placeholder)

# assigning variable to the guessed letter

guess = input("Guess a letter: ").lower()

# adding a display that puts the guess letter in the right position and _ in the rest of the string

display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)

# Checking does the guessed letter present in the chosen word

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
