# Program 27: Display specific columns (Name and Marks) from a CSV file
import csv

try:
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)
        print("--- Name and Marks ---")
        for row in reader:
            print(f"Name: {row['Name']}, Marks: {row['Marks']}")

except FileNotFoundError:
    print("Error: 'students.csv' file not found.")
