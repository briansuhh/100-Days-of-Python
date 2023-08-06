import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
ans = input("What do you choose? (rock | paper | scissors) ")
print(f"\nYou chose {ans}.")
if ans == "rock":
    print(rock)
elif ans == "paper":
    print(paper)
elif ans == "scissors":
    print(scissors)
else:
    exit()

choices = ["rock", "paper", "scissors"]
chosen = random.choice(choices)

win = 0
draw = 0
print(f"The computer chose {chosen}.")
if chosen == "rock":
    print(rock)
    if ans == "paper":
        win = 1
    elif ans == "rock":
        draw = 1
    else:
        win = 0
elif chosen == "paper":
    print(paper)
    if ans == "scissors":
        win = 1
    elif ans == "paper":
        draw = 1
    else:
        win = 0
elif chosen == "scissors":
    print(scissors)
    if ans == "rock":
        win = 1
    elif ans == "scissors":
        draw = 1
    else:
        win = 0

if win == 1:
    print("You win.")
elif draw == 1:
    print("It's a draw")
else:
    print("You lose.")
