# 25. Count word frequency in a given paragraph using a dictionary. 

# Given paragraph
paragraph = "python is easy and python is powerful"

# Convert paragraph into words
words = paragraph.split()

# Count word frequency
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Display the word frequency
print("Word frequency:", word_count)