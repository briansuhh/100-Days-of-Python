import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def current_card():
    print(f"\tYour cards: {player_card}, current score: {player_score}")
    print(f"\tComputer's first card: {dealer_card[0]}")  

def final_card():
    print(f"\tYour final hand: {player_card}, final score: {player_score}")
    print(f"\tComputer's final hand: {dealer_card}, final score: {dealer_score}")

while 1:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        os.system('clear')
        #display logo - d pa kailangan

        player_card = []
        dealer_card = []
        # loop 2 times to give 2 cards for the player and dealer
        for i in range(0, 2):
            player_card.append(random.choice(cards))
            dealer_card.append(random.choice(cards))
        
        # get the score of the player by looping through the list and adding all
        player_score = 0
        print_once = False
        for card in player_card:
            player_score += card
            #determine if ace will have a value of 1 or 11
            if player_score >= 21 and card == 11:
                player_score -= 10
                if not print_once:
                    print("\nSince there is already one ace, all additional aces will have a value of 1.")
                    print_once = True

        #show 2 cards of the player and 1 card for the dealer
        current_card()

        #check if the total of the dealer is below 17, pick another card
        dealer_score = 0
        for card in dealer_card:
            dealer_score += card
            if dealer_score >= 21 and card == 11:
                dealer_score -= 10
        while dealer_score < 17:
            dealer_card.append(random.choice(cards))
            dealer_score += dealer_card[len(dealer_card) - 1]

        while player_score < 21:
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                player_card.append(random.choice(cards))
                player_score += player_card[len(player_card) - 1]
                current_card()
            else:
                break

        if player_score > 21:
            final_card()
            print("\nYou went over 21. You lose.\n")
        elif dealer_score > 21:
            final_card()
            print("\nOpponent went over 21. You win.\n")
        elif dealer_score == player_score:
            final_card()
            print("It's a tie.")
        elif dealer_score > player_score:
            final_card()
            print("\nYou lose.\n")
        else:
            final_card()
            print("\nYou win.\n")
    else:
        exit()


