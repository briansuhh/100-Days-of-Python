import string 
characters = list(string.ascii_lowercase)

# choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))

# get the index of all the letters on the message based on the alphabet and add the shift number
indexes = []
result = []
for i in range(0, len(message)):
    indexes.append(characters.index(message[i]))
    indexes[i] += shift
    result.append(characters[indexes[i]])

result = ''.join(str (item) for item in result)
print(f"Here's the encoded result:{result}")