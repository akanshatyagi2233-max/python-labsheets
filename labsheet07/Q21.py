# Program 21: Create and write data into a CSV file
import csv

data = [
    ["Name", "RollNo", "Marks"],
    ["Aarav", "101", "85"],
    ["Priya", "102", "92"],
    ["Rahul", "103", "78"]
]

try:
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("CSV file 'students.csv' created and populated successfully.")

except IOError as e:
    print(f"An I/O error occurred: {e}")
