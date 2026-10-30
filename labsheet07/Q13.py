
# Program 13: Read numbers from a file and display their sum and average

try:
    with open("numbers.txt", "r") as file:
        content = file.read()
        # Convert space/newline separated strings into integers or floats
        numbers = [float(num) for num in content.split()]

    if len(numbers) > 0:
        total_sum = sum(numbers)
        average = total_sum / len(numbers)
        print(f"Numbers found: {numbers}")
        print(f"Sum: {total_sum}")
        print(f"Average: {average}")
    else:
        print("The file contains no numbers.")

except FileNotFoundError:
    print("Error: The file 'numbers.txt' was not found.")
except ValueError:
    print("Error: File contains non-numeric data.")