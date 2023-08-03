# Exercise 1 - Odd or Even
- Instructions:
Write a program that works out whether if a given number is an odd or even number.

- Input:
43
94

- Output:
This is an odd number.
This is an even number.

- Code:
```py
num = int(input("Which number do you want to check? "))
if num % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
```

# Exercise 2 - BMI 2.0
- Instructions:
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

- Input:
weight = 85
height = 1.75   

- Output:
Your BMI is 28, you are slightly overweight.

- Code:
```py
height = float(input("enter you height in m: "))
weight = float(input("enter you weight in kg: "))

bmi = weight / height ** 2
bmi = round(bmi)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
```

# Exercise 3 - Leap Year
- Instructions:
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.

- Input:
2400
1989

- Output:
Leap year.
Not leap year.

- Code:
```py

```
