# Program 7: Write multiple lines of input from the user into a file

try:
    with open("user_input.txt", "w") as file:
        print("Enter text to write into the file. Type 'STOP' on a new line to finish:")
        while True:
            user_line = input()
            if user_line == "STOP":
                break
            file.write(user_line + "\n")

    print("User input successfully written to 'user_input.txt'.")

except IOError as e:
    print(f"An I/O error occurred: {e}")
