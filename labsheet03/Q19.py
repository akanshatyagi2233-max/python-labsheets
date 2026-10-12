# 19. Find the most repeated word in a string. 

# Take input from the user
s = input("Enter a string: ")

# Convert the string to lowercase and split it into words
words = s.lower().split()

# Create an empty dictionary to count words
frequency = {}

# Count the frequency of each word
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Find the most repeated word
if frequency:
    max_word = max(frequency, key=frequency.get)
    print("Most repeated word:", max_word)
    print("Frequency:", frequency[max_word])
else:
    print("No words found.")
