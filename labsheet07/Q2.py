# Program 2: Read the entire content of a text file

try:
    # Open 'sample.txt' in read mode ('r')
    with open("sample.txt", "r") as file:
        content = file.read()  # Read the entire file content into a string

    print("--- File Content ---")
    print(content)

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except IOError as e:
    print(f"An I/O error occurred: {e}")
