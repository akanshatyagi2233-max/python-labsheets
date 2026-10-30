# Program 11: Search for a particular word in a file

search_word = "Python"
found = False

try:
    with open("sample.txt", "r") as file:
        for line_no, line in enumerate(file, 1):
            if search_word in line:
                print(f"Found '{search_word}' on line {line_no}: {line.strip()}")
                found = True

    if not found:
        print(f"The word '{search_word}' was not found in the file.")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
