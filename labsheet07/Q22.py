# Program 22: Read data from a CSV file and display it
import csv

try:
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        print("--- CSV File Contents ---")
        for row in reader:
            print(row)

except FileNotFoundError:
    print("Error: 'students.csv' file not found.")
