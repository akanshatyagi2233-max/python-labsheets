
import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="akansha07",
        database="student_db"
    )

    cursor = con.cursor()

    cursor.execute("DESC students")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    con.close()

except mysql.connector.Error as e:
    print("Error:", e)