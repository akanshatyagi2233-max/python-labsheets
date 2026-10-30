# Program 3: Read a file line by line

try:
    with open("sample.txt", "r") as file:
        print("--- Reading File Line by Line ---")
        # Iterate over the file object directly to read line by line efficiently
        for line in file:
            print(line.strip())  # strip() removes trailing newline characters

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
