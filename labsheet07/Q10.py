# Program 10: Read a file and convert its content to uppercase

try:
    with open("sample.txt", "r") as file:
        content = file.read()

    print("--- Uppercase File Content ---")
    print(content.upper())

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
