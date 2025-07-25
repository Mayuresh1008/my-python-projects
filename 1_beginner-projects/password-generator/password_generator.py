import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")

# Easy Version
""" 
password = ""

nr_letters = int(input("How many letters do you want to add in the password? "))
nr_numbers = int(input("How many numbers do you want to add in the password? "))
nr_symbols = int(input("How many symbols do you want to add in the password? "))

for char in range(0, nr_letters):
    password += random.choice(letters)

for char in range(0, nr_numbers):
    password += random.choice(numbers)

for char in range(0, nr_symbols):
    password += random.choice(symbols)

print("Your Password: ", password)
"""

# Hard Version
password_list = []

nr_letters = int(input("How many letters do you want to add in the password? "))
nr_numbers = int(input("How many numbers do you want to add in the password? "))
nr_symbols = int(input("How many symbols do you want to add in the password? "))

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

# print(password_list) # password before shuffling
random.shuffle(password_list)
# print(password_list) # password after shuffling

password = ""
for char in password_list:
    password += char

print("Here's Your Password:", password)
