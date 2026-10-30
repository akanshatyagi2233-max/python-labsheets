# Program 18: Read a file and store only unique words into another file

try:
    with open("sample.txt", "r") as file:
        text = file.read()
        words = text.split()

    # Use a set to extract unique words
    unique_words = sorted(set(words))

    with open("unique_words.txt", "w") as file:
        for word in unique_words:
            file.write(word + "\n")

    print("Unique words successfully stored in 'unique_words.txt'.")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
