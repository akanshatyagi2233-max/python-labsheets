# 30. Create a dictionary from a string with characters as keys and frequency as values. 

# Given string
text = "programming"

# Create an empty dictionary
char_count = {}

# Count character frequency
for char in text:
    char_count[char] = char_count.get(char, 0) + 1

# Display the dictionary
print("Character frequency:", char_count)