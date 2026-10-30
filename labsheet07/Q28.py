# Program 28: Find and display the highest marks from a CSV file
import csv

try:
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)
        top_student = None
        max_marks = -1.0

        for row in reader:
            marks = float(row["Marks"])
            if marks > max_marks:
                max_marks = marks
                top_student = row["Name"]

        if top_student:
            print(f"Top Student: {top_student} with Marks: {max_marks}")
        else:
            print("No records found.")

except FileNotFoundError:
    print("Error: 'students.csv' file not found.")
