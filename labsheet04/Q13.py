# 13. Count the frequency of characters in a string using a dictionary.

# Count the frequency of characters in a string
string = input("Enter a string: ")

frequency = {}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequency:", frequency)

