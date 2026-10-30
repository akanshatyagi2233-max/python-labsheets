# Program 20: Merge two text files into a third file

try:
    with open("file1.txt", "w") as f1:
        f1.write("Content from File 1.\n")
    with open("file2.txt", "w") as f2:
        f2.write("Content from File 2.\n")

    # Merge into merged.txt
    with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as merged:
        merged.write(f1.read())
        merged.write("\n")
        merged.write(f2.read())

    print("Successfully merged 'file1.txt' and 'file2.txt' into 'merged.txt'.")

except IOError as e:
    print(f"An I/O error occurred: {e}")
