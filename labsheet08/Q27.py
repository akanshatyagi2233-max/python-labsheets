import mysql.connector
import csv

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="akansha07",
        database="student_db"
    )

    cursor = con.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS imported_students (
            id INT,
            name VARCHAR(50),
            age INT,
            marks FLOAT
        )
    """)

    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            cursor.execute(
                "INSERT INTO imported_students VALUES (%s, %s, %s, %s)",
                row
            )

    con.commit()

    print("CSV data imported successfully!")

    cursor.close()
    con.close()

except Exception as e:
    print("Error:", e)
