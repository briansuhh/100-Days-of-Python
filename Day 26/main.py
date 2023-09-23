#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

data = pandas.read_csv("Day 26/nato_phonetic_alphabet.csv")

nato_aplhabet = {row.letter:row.code for index, row in data.iterrows()}

input_word = input("Enter a word: ").upper()

output_list = [nato_aplhabet[letter] for letter in input_word]

print(output_list)