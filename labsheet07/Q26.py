# Program 26: Copy data from one CSV file to another
import csv

try:
    with open("students.csv", "r") as src, open("students_backup.csv", "w", newline="") as dest:
        reader = csv.reader(src)
        writer = csv.writer(dest)
        for row in reader:
            writer.writerow(row)

    print("Data successfully copied from 'students.csv' to 'students_backup.csv'.")

except FileNotFoundError:
    print("Error: 'students.csv' file not found.")
