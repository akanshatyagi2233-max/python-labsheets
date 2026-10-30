# Program 16: Display the first and last lines of a file

try:
    with open("sample.txt", "r") as file:
        lines = file.readlines()

    if lines:
        print(f"First Line: {lines[0].strip()}")
        print(f"Last Line: {lines[-1].strip()}")
    else:
        print("The file is empty.")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
