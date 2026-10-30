import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="akansha07",
        database="student_db"
    )

    cursor = con.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")

    result = cursor.fetchone()

    print("Total number of students:", result[0])

    cursor.close()
    con.close()

except mysql.connector.Error as e:
    print("Error:", e)
