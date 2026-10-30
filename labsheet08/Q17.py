import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="akansha07",
        database="student_db"
    )

    cursor = con.cursor()

    sql = "UPDATE students SET name = %s WHERE id = %s"

    values = ("Akansha Tyagi", 1)

    cursor.execute(sql, values)
    con.commit()

    print("Student name updated successfully!")

    cursor.close()
    con.close()

except mysql.connector.Error as e:
    print("Error:", e)
