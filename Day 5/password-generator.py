import random
import string

print("Welcome to the PyPassword Generator")
letter_count = int(input("How many letters would you like in your password?\n"))
num_count = int(input("How many numbers would you like?\n"))
symbol_count = int(input("How many symbols would you like?\n"))

password = []
letter = list(string.ascii_letters)
for i in range(letter_count):
    index = random.randint(0, len(letter) - 1)
    password.append(letter[index])

num = list(string.digits)
for i in range(num_count):
    index = random.randint(0, len(num) - 1)
    password.append(num[index])

symbol = list(string.punctuation)
for i in range(symbol_count):
    index = random.randint(0, len(symbol) - 1)
    password.append(symbol[index])

random.shuffle(password)
password = ''.join(str(item) for item in password)
print(f"Your password is: {password}")