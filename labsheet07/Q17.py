# Program 17: Remove blank lines from a file

try:
    with open("sample.txt", "r") as file:
        lines = file.readlines()

    # Filter out lines that are empty or contain only whitespace
    non_blank_lines = [line for line in lines if line.strip() != ""]

    # Write back the non-blank lines
    with open("sample.txt", "w") as file:
        file.writelines(non_blank_lines)

    print("Blank lines successfully removed from the file.")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
