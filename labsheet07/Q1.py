
# Program 1: Create and write text into a file

try:
    # Open 'sample.txt' in write mode ('w')
    # The 'with' statement ensures the file is automatically closed after writing
    with open("sample.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("Welcome to COER University Python Programming Lab.\n")
        file.write("File handling in Python is simple and powerful.\n")

    print("Data successfully written to 'sample.txt'.")

except IOError as e:
    print(f"An I/O error occurred: {e}")