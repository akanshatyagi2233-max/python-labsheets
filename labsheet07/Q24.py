# Program 24: Count the number of rows and columns in a CSV file
import csv

try:
    with open("students.csv", "r") as file:
        reader = list(csv.reader(file))
        if reader:
            row_count = len(reader)
            col_count = len(reader[0])
            print(f"Total Rows (including header): {row_count}")
            print(f"Total Columns: {col_count}")
        else:
            print("The CSV file is empty.")

except FileNotFoundError:
    print("Error: 'students.csv' file not found.")
