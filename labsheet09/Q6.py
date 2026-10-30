employees = {}

while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        emp_id = input("Enter ID: ")
        name = input("Enter name: ")
        employees[emp_id] = name
        print("Employee added!")

    elif choice == 2:
        print(employees)

    elif choice == 3:
        emp_id = input("Enter ID: ")
        if emp_id in employees:
            employees[emp_id] = input("Enter new name: ")
            print("Employee updated!")
        else:
            print("Employee not found")

    elif choice == 4:
        emp_id = input("Enter ID: ")
        if emp_id in employees:
            del employees[emp_id]
            print("Employee deleted!")
        else:
            print("Employee not found")

    elif choice == 5:
        break

    else:
        print("Invalid choice")
