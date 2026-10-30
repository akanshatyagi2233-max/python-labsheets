# Program 9: Copy the contents of one file into another

try:
    # Open source file for reading and destination file for writing
    with open("sample.txt", "r") as src_file, open("destination.txt", "w") as dest_file:
        for line in src_file:
            dest_file.write(line)

    print("Contents successfully copied from 'sample.txt' to 'destination.txt'.")

except FileNotFoundError:
    print("Error: Source file not found.")
except IOError as e:
    print(f"An I/O error occurred: {e}")
