with open("file1.txt") as file:
    file_1 = file.readlines()

with open("file2.txt") as file:
    file_2 = file.readlines()

result = [int(n) for n in file_1 if n in file_2]

# Write your code above 👆

print(result)


