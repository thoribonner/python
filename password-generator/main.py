import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

character_types = [letters, symbols, numbers]

length = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17 ]

random_length = random.choice(length) + 1

password = ''

for i in range(1, random_length):
  character_type = random.choice(character_types)
  character = random.choice(character_type)
  password += character

print(f'Your new password: {password}')