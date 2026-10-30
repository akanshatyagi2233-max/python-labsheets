
# Program 19: Sort all words in a file alphabetically and save to a new file

try:
    with open("sample.txt", "r") as file:
        text = file.read()
        words = text.split()

    # Sort words alphabetically
    words.sort()

    with open("sorted_words.txt", "w") as file:
        for word in words:
            file.write(word + "\n")

    print("Alphabetically sorted words saved to 'sorted_words.txt'.")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")