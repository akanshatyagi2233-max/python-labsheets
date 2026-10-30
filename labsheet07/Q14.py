# Program 14: Display the longest line in a file

try:
    with open("sample.txt", "r") as file:
        lines = file.readlines()

    if lines:
        # Find the line with the maximum length (excluding trailing whitespaces/newlines)
        longest_line = max(lines, key=lambda x: len(x.strip()))
        print("--- Longest Line ---")
        print(longest_line.strip())
    else:
        print("The file is empty.")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
