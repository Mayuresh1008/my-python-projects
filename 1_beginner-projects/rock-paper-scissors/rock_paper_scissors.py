import random
import sys

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]
user_choice = int(
    input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors.\n")
)


if user_choice >= 0 and user_choice <= 2:
    print("You chose:")
    print(game_images[user_choice])
else:
    sys.exit("You typed an invalid input. You lose.")

computer_choice = random.randint(0, 2)

print("Computer chose:")
print(game_images[computer_choice])

if (
    (user_choice == 0 and computer_choice == 2)
    or (user_choice == 1 and computer_choice == 0)
    or (user_choice == 2 and computer_choice == 1)
):
    print("You WIn!")
elif user_choice == computer_choice:
    print("It's a draw")
else:
    print("You lose")
