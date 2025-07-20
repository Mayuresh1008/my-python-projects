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

game_over = False
correct_letters = []

# Using a while loop to let the user guess again.

while not game_over:

    # assigning variable to the guessed letter

    guess = input("Guess a letter: ").lower()

    # adding a display that puts the guess letter in the right position and _ in the rest of the string

    display = ""

    # Changing the for loop so that it can keep the previous correct letters in display

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You Win")
