# Exercise 1 - Banker Roulette
- Instructions:<br>
You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.<br>
Important: You are not allowed to use the choice() function.

- Input:<br>
Angela, Ben, Jenny, Michael, Chloe

- Output:<br>
Michael is going to buy the meal today!

- Code:
```py
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

index = random.randint(0, len(names) - 1)
print(f"{names[index]} is going to buy the meal today!")
```