# Program 5: Count the number of lines and characters in a file

try:
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        line_count = len(lines)
        
        # Calculate total characters by joining the lines or reading the full text
        file.seek(0)  # Reset file pointer to the beginning
        content = file.read()
        char_count = len(content)

    print(f"Total number of lines: {line_count}")
    print(f"Total number of characters: {char_count}")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
