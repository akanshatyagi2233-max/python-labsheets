# Program 12: Count the occurrence of a specific word in a file

target_word = "Python"

try:
    with open("sample.txt", "r") as file:
        text = file.read()
        # Split text into words and count exact matches (ignoring case if needed)
        words = text.split()
        count = words.count(target_word)

    print(f"The word '{target_word}' occurs {count} time(s) in the file.")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
