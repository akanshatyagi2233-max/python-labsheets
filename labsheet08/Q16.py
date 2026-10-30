import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="akansha07",
        database="student_db"
    )

    cursor = con.cursor()

    sql = "UPDATE students SET marks = %s WHERE id = %s"

    values = (95, 1)

    cursor.execute(sql, values)
    con.commit()

    print("Student marks updated successfully!")

    cursor.close()
    con.close()

except mysql.connector.Error as e:
    print("Error:", e)
