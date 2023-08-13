## Exercise 1 - Printing
- Instructions:<br>
Write a program in main.py that prints the same notes from the previous lesson

- Output:<br>
Day 1 - Python Print Function<br>
The function is declared like this:<br>
print('what to print')

- Code:
```python
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")
```

## Exercise 2 - Debugging Practice
- Instructions:<br>
Look at the code in the code editor on the right. There are errors in all of the lines of code. Fix the code so that it runs without errors.

- Code with errror:
```py
print(Day 1 - String Manipulation)
print(String Concatenation is done with the "+" sign.)
print('e.g. print("Hello " + "world))
print(New lines can be created with a backslash and n.")
```

- Output:<br>
Day 1 - String Manipulation<br>
String Concatenation is done with the "+" sign.<br>
e.g. print("Hello " + "world")<br>
New lines can be created with a backslash and n.

-Code:
```py
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
```

## Exercise 3 - Input Function
- Instructions:<br>
Write a program that prints the number of characters in a user's name.

- Input:<br>
Angela

- Output:<br>
6

- Code:
```py
name = input("What is your name? ")
print(len(name))
```

## Exercise 4 - Variable
- Instructions:<br>
Write a program that switches the values stored in the variables a and b.

- Input:<br>
a: 3<br>
b: 5

- Output:<br>
a: 5<br>
b: 3

- Code:
```py
a = input("a: ")
b = input("b: ")

temp = a
a = b
b = temp

print(f"a: {a}")
print(f"b: {b}")
```

## Project: Band Name Generator
- Code:
```py
print("Greetings! This program generates a name for your program\n")
city = input("What city did you grew up in? ")
pet = input("What is the name of your pet? ")
print(f"\nYour band name is {city} {pet}.")
```

- Output:
![Band Name Generator](/d/Files/Programming/100 Days of Code Python/assets/img/code.png)