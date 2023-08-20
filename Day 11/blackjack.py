import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def current_card():
    print(f"\tYour cards: {player_card}, current score: {player_score}")
    print(f"\tComputer's first card: {dealer_card[0]}")  

def final_card():
    print(f"\n\tYour final hand: {player_card}, final score: {player_score}")
    print(f"\tComputer's final hand: {dealer_card}, final score: {dealer_score}")

while 1:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        os.system('clear')

        player_card = []
        dealer_card = []
        for i in range(0, 2):
            player_card.append(random.choice(cards))
            dealer_card.append(random.choice(cards))
        
        player_score = 0
        print_once = False
        for card in player_card:
            player_score += card
            if player_score >= 21 and card == 11:
                player_score -= 10
                if not print_once:
                    print("\nSince there is already one ace, all additional aces will have a value of 1.")
                    print_once = True

        dealer_score = 0
        for card in dealer_card:
            dealer_score += card
            if dealer_score >= 21 and card == 11:
                dealer_score -= 10
                
        while dealer_score < 17:
            dealer_card.append(random.choice(cards))
            dealer_score += dealer_card[len(dealer_card) - 1]

        current_card()

        while player_score < 21:
            if input("\nType 'y' to get another card, type 'n' to pass: ") == 'y':
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
            print("\nIt's a tie.\n")
        elif dealer_score > player_score:
            final_card()
            print("\nYou lose.\n")
        else:
            final_card()
            print("\nYou win.\n")
    else:
        exit()