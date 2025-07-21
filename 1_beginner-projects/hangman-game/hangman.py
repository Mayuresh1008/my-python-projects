import random

# importing word list from the hangman_words.py file
from hangman_words import word_list

# importing logo and stages from the hangman_art.py file
from hangman_art import logo, stages

print(logo)

# assigining a variable for keeping track of number of lives left.
lives = 6

# assigining variable to the random word
chosen_word = random.choice(word_list)

# adding placeholder with same numbers of blanks as the chosen_word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

# Using a while loop to let the user guess again.

while not game_over:
    print(
        f"****************************{lives}/6 LIVES LEFT****************************"
    )

    # assigning variable to the guessed letter

    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You,ve already guessed {guess}")

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

    print("Word to guess: " + display)

    # adding a if statement that tracks if the guess letter is not in the chosen_word then it reduces the lives by 1
    # and if the lives becomes equals to zero then the game should stop and it will print "You lose."
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True

            print(
                f"***********************IT WAS {chosen_word}! YOU LOSE**********************"
            )

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # adding the ASCII art of stages corresponding to the number of lives left
    print(stages[lives])
