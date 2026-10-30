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
    cursor.execute("SELECT * FROM students")

    records = cursor.fetchall()

    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([i[0] for i in cursor.description])
        writer.writerows(records)

    print("Data exported successfully to students.csv")

    cursor.close()
    con.close()

except mysql.connector.Error as e:
    print("Error:", e)
