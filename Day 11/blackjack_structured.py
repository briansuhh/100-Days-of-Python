import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def get_card(cards):
    return random.choice(cards)

def calculate_score(card_list):
    score = 0
    for i in range(0, len(card_list)):
        score += card_list[i]
        if score > 21 and card_list[i] == 11:
            score -= 10
            card_list[i] -= 10
    return score  

def display_card(player_card, dealer_card, player_score):
    print(f"\tYour cards: {player_card}, current score: {player_score}")
    print(f"\tComputer's first card: {dealer_card[0]}")  

def blackjack_game():
    while 1:
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
            os.system('clear')
            player_card = []
            dealer_card = []
            for _ in range(0, 2):
                player_card.append(get_card(cards))
                dealer_card.append(get_card(cards))

            player_score = calculate_score(player_card)
            dealer_score = calculate_score(dealer_card)
            display_card(player_card, dealer_card, player_score)

            while dealer_score < 17:
                dealer_card.append(get_card(cards))
                dealer_score = calculate_score(dealer_card)

            while player_score < 21:
                if input("\nType 'y' to get another card, type 'n' to pass: ") == 'y':
                    player_card.append(get_card(cards))
                    player_score = calculate_score(player_card)
                    display_card(player_card, dealer_card, player_score)
                else:
                    break

            print(f"\n\tYour final hand: {player_card}, final score: {player_score}")
            print(f"\tComputer's final hand: {dealer_card}, final score: {dealer_score}")
            
            if player_score > 21:
                print("\nYou went over 21. You lose.\n")
            elif dealer_score > 21:
                print("\nOpponent went over 21. You win.\n")
            elif dealer_score == player_score:
                print("\nIt's a tie.\n")
            elif dealer_score > player_score:
                print("\nYou lose.\n")
            else:
                print("\nYou win.\n")
        else:
            exit()

if __name__ == "__main__":
    blackjack_game()