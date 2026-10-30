# Program 4: Count the number of words in a text file

try:
    with open("sample.txt", "r") as file:
        text = file.read()
        # Split the text by whitespace to get a list of words
        words = text.split()
        word_count = len(words)

    print(f"Total number of words in the file: {word_count}")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
