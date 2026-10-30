# Program 29: Search a record in a CSV file based on student name
import csv

search_name = "Priya"
found = False

try:
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"].lower() == search_name.lower():
                print(f"Record Found -> Name: {row['Name']}, RollNo: {row['RollNo']}, Marks: {row['Marks']}")
                found = True
                break

    if not found:
        print(f"Student '{search_name}' not found in records.")

except FileNotFoundError:
    print("Error: 'students.csv' file not found.")
