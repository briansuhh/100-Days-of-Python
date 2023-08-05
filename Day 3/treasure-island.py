print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("Pick your own path.")
direction = input("\nWhich way do you want to go? (left | right) ")

if direction == 'left':
    print()
else:
    print("You fell into a hole.\nGame Over.")
    exit()

if_swim = input("You found a river. What will you do? (swim | wait) ")

if if_swim == "wait":
    print()
else:
    print("You got attacked by a trout.\nGame Over.")
    exit()

door = input("You waited and a door popped right infront of you. Which door will you pick? (red | blue | yellow) ")

if door == "red":
    print("\nYou got burned by fire.\nGame Over.")
elif door == "blue":
    print("\nYou got eaten by beasts.\nGame Over.")
elif door == "yellow":
    print("\nCongratulations! You Win!")
else:
    print("\nGame Over.")