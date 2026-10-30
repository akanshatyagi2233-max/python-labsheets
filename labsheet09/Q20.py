import mysql.connector

# Connect to database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="akansha07",
    database="college"
)

cur = con.cursor()

while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sid = int(input("Enter ID: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))

        cur.execute(
            "INSERT INTO students VALUES (%s,%s,%s,%s)",
            (sid, name, age, marks)
        )
        con.commit()
        print("Student added successfully!")

    elif choice == "2":
        cur.execute("SELECT * FROM students")
        records = cur.fetchall()

        for row in records:
            print(row)

    elif choice == "3":
        sid = int(input("Enter ID: "))
        marks = float(input("Enter new marks: "))

        cur.execute(
            "UPDATE students SET marks=%s WHERE id=%s",
            (marks, sid)
        )
        con.commit()

        if cur.rowcount > 0:
            print("Student updated successfully!")
        else:
            print("Student not found")

    elif choice == "4":
        sid = int(input("Enter ID: "))

        cur.execute(
            "DELETE FROM students WHERE id=%s",
            (sid,)
        )
        con.commit()

        if cur.rowcount > 0:
            print("Student deleted successfully!")
        else:
            print("Student not found")

    elif choice == "5":
        print("Program closed!")
        break

    else:
        print("Invalid choice!")

cur.close()
con.close()
