import json
import os

filename = "records.json"

def load_data():
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

while True:
    print("\n1. Add Record")
    print("2. View Records")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Exit")

    choice = input("Enter choice: ")
    records = load_data()

    if choice == "1":
        name = input("Enter name: ")
        records.append({"name": name})
        save_data(records)
        print("Record added!")

    elif choice == "2":
        print(records)

    elif choice == "3":
        name = input("Enter old name: ")
        found = False
        for record in records:
            if record["name"] == name:
                record["name"] = input("Enter new name: ")
                found = True
                break
        if found:
            save_data(records)
            print("Record updated!")
        else:
            print("Record not found")

    elif choice == "4":
        name = input("Enter name to delete: ")
        new_records = [r for r in records if r["name"] != name]
        if len(new_records) < len(records):
            save_data(new_records)
            print("Record deleted!")
        else:
            print("Record not found")

    elif choice == "5":
        break

    else:
        print("Invalid choice")
