import string 
characters = list(string.ascii_lowercase)
while 1:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    # get the index of all the letters on the message based on the alphabet and add the shift number
    result = ''
    for char in message:
        if char in characters:
            index = characters.index(char)
            if choice == "encode":
                index = (index + shift) % 26
            if choice == "decode":
                index = (index - shift) % 26
            result += characters[index]
        else:
            result += char

    print(f"Here's the result: {result}")

    user_choice = input("Do you want to try again? (yes/no) ")
    if user_choice == "yes":
        continue
    else:
        break