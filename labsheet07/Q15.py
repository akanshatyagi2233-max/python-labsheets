# Program 15: Replace a word in a file with another word

old_word = "Python"
new_word = "Java"

try:
    # Read the file content
    with open("sample.txt", "r") as file:
        content = file.read()

    # Replace the word
    updated_content = content.replace(old_word, new_word)

    # Write the modified content back to the file
    with open("sample.txt", "w") as file:
        file.write(updated_content)

    print(f"Successfully replaced all instances of '{old_word}' with '{new_word}'.")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
