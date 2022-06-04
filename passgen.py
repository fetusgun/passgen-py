# -----------------------------------------
# A simple password generator in python for
# learning purposes
# Author: Paulo Ferr
# Date: 04/06/2022
# -----------------------------------------

import random

# Lists of Letters, Symbols and numbers to choose
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("****** | Password Generator | ******")
number_of_letters = int(input("Choose how many letters goes in your password: \n")) 
number_of_symbols = int(input(f"How many symbols?\n"))
number_of_numbers = int(input(f"How many numbers?\n"))

password_list = []

# pick the letters from the list
for character in range(1, number_of_letters + 1):
    password_list.append(random.choice(letters))

# pick the symbols from the list
for character in range(1, number_of_symbols + 1):
    password_list.append(random.choice(symbols))

# pick the numbers from the list
for character in range(1, number_of_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for character in password_list:
    password += character

print(f"Your generated password is > {password}")