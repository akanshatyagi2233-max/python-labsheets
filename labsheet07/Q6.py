# Program 6: Display only even-numbered lines from a file

try:
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        print("--- Even-Numbered Lines ---")
        # enumerate starts at index 0, so line number = index + 1
        for index, line in enumerate(lines):
            line_number = index + 1
            if line_number % 2 == 0:
                print(f"Line {line_number}: {line.strip()}")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
