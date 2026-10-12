# 16. Count the number of digits, alphabets, and special characters in a string. 

s = input("Enter a string: ")

digits = 0
alphabets = 0
special = 0

# Check each character in the string
for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        alphabets += 1
    else:
        special += 1

# Display the results
print("Number of digits:", digits)
print("Number of alphabets:", alphabets)
print("Number of special characters:", special)
