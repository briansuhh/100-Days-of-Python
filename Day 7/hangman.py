import os
import string
import random
import hangman_art as art
import hangman_words as words

word = random.choice(words.word_list)
guessed_letters = []
characters = list(string.ascii_lowercase)
lives = 6

print(art.title)    
while 1:
    for i in characters:
        print(i, end=" ")
    letter = input("\nGuess a letter: ") 
    os.system("clear")

    print()
    found = False
    for i in word:
        if i == letter:
            print(f"{letter}", end=" ")
            found = True
        elif i in guessed_letters:
            print(i, end=" ")
        else: 
            print("_", end=" ")

    if found:
        print(f"\n\nYou guessed {letter}")
    else:
        lives -= 1
        print(f"\n\nYou guessed {letter}, that's not in the word. You lose a life.")

    if letter in guessed_letters:
        print("You already guessed that letter")  
    else:
        guessed_letters.append(letter)

    for i in range(0, 7):
        if lives == i:
            print(art.phase[i])

    if all(i in characters for i in letter):
        try:
            characters.remove(letter)
        except ValueError:
            print("Invalid input. Please enter a valid letter.\n")

    # To check all the letter in the word if it is in the guessed_letters list
    if all(i in guessed_letters for i in word):
        print("Congratulations! You have succesfully completed the game.")
        break

    if lives == 0:
        print("You lose.")
        break