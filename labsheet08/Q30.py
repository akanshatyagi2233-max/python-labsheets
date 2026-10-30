import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="akansha07",
        database="student_db"
    )

    cursor = con.cursor()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Marks")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            id = int(input("Enter ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            marks = float(input("Enter Marks: "))

            cursor.execute(
                "INSERT INTO students VALUES (%s, %s, %s, %s)",
                (id, name, age, marks)
            )
            con.commit()
            print("Student added successfully!")

        elif choice == "2":
            cursor.execute("SELECT * FROM students")

            for row in cursor.fetchall():
                print(row)

        elif choice == "3":
            id = int(input("Enter Student ID: "))
            marks = float(input("Enter New Marks: "))

            cursor.execute(
                "UPDATE students SET marks=%s WHERE id=%s",
                (marks, id)
            )
            con.commit()
            print("Student updated successfully!")

        elif choice == "4":
            id = int(input("Enter Student ID: "))

            cursor.execute(
                "DELETE FROM students WHERE id=%s",
                (id,)
            )
            con.commit()
            print("Student deleted successfully!")

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")

    cursor.close()
    con.close()

except mysql.connector.Error as e:
    print("Database Error:", e)
