print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

couple = name1 + name2

# true count
count1 = 0
count1 += couple.count('t')
count1 += couple.count('r')
count1 += couple.count('u')
count1 += couple.count('e')
count1 *= 10

# love count
count2 = 0
count2 += couple.count('l')
count2 += couple.count('o')
count2 += couple.count('v')
count2 += couple.count('e')

count = count1 + count2

if count < 10 or count > 90:
    print(f"Your score is {count}, you go together like coke and mentos.")
elif count > 40 and count < 50:
    print(f"Your score is {count}, you are alright together.")
else:
    print(f"Your score is {count}.")