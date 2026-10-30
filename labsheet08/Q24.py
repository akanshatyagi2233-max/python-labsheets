import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="akansha07",
        database="student_db"
    )

    cursor = con.cursor()

    cursor.execute("SELECT AVG(marks) FROM students")

    result = cursor.fetchone()

    print("Average Marks:", result[0])

    cursor.close()
    con.close()

except mysql.connector.Error as e:
    print("Error:", e)
