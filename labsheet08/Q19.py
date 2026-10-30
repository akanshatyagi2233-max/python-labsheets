import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="akansha07",
        database="student_db"
    )

    cursor = con.cursor()

    cursor.execute("DELETE FROM students WHERE marks < 40")
    con.commit()

    print(cursor.rowcount, "Student records deleted!")

    cursor.close()
    con.close()

except mysql.connector.Error as e:
    print("Error:", e)
