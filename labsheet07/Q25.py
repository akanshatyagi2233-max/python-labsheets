# Program 25: Append a new record to an existing CSV file
import csv

new_record = ["Neha", "104", "95"]

try:
    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(new_record)

    print("New record successfully appended to 'students.csv'.")

except IOError as e:
    print(f"An I/O error occurred: {e}")
