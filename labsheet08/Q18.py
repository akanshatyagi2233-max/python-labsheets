import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="akansha07",
        database="student_db"
    )

    cursor = con.cursor()

    sql = "DELETE FROM students WHERE id = %s"

    values = (4,)

    cursor.execute(sql, values)
    con.commit()

    print("Student record deleted successfully!")

    cursor.close()
    con.close()

except mysql.connector.Error as e:
    print("Error:", e)
