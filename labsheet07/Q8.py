
# Program 8: Append new content to an existing file

try:
    # Open file in append mode ('a') so existing content is preserved
    with open("sample.txt", "a") as file:
        file.write("This is a newly appended line.\n")

    print("New content successfully appended to 'sample.txt'.")

except IOError as e:
    print(f"An I/O error occurred: {e}")