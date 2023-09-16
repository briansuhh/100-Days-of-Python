#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


# These 2 script are the same, but the second one is more efficient
# in the second way, we don't need to store the names in a list, we can just iterate over the file itself
# and we don't need to store the letter in a variable, we can just read it and use it directly in the loop


# First way
# with open("Input/Names/invited_names.txt") as names:
#     names = names.readlines()

# with open("Input/Letters/starting_letter.txt") as letter:
#     letter_content = letter.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_content.replace("[name]", stripped_name)
#         with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)



# # More efficient way
# with open("Input/Letters/starting_letter.txt") as letters:
#     letter_content = letters.read()
#     with open("Input/Names/invited_names.txt") as names:
#         for name in names:
#             stripped_name = name.strip()
#             new_letter = letter_content.replace("[name]", stripped_name)
#             with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#                 completed_letter.write(new_letter)


