# Program 23: Read a CSV file and calculate the average of numeric columns (Marks)
import csv

try:
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)
        marks = []
        for row in reader:
            marks.append(float(row["Marks"]))

        if marks:
            avg_marks = sum(marks) / len(marks)
            print(f"Average Marks: {avg_marks:.2f}")
        else:
            print("No numeric data found in the 'Marks' column.")

except FileNotFoundError:
    print("Error: 'students.csv' file not found.")
except ValueError:
    print("Error: Non-numeric data encountered in numeric column.")
