import os
auction = {}
# create a while loop to get all the auctioner's bid and add it on the dictionary
while 1:
    name = input("What is your name: ")
    bid = int(input("Input your bid: "))

    #put it inside the dictionary
    auction[name] = bid 

    user_choice = input("Is there another bidder? (yes/no) ")
    if user_choice == "yes":
        os.system('clear')
        continue
    else:
        # print the highest bidder by looping throuh the dictionary
        highest = 0
        for people in auction:
            if auction[people] > highest:
                name = people
                highest = auction[people]
        os.system('clear')
        print(f"The winner is {name} with a bid of {highest}")
        break