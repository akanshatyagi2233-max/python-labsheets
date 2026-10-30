import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="akansha07",
        database="student_db"
    )

    cursor = con.cursor()

    sql = "INSERT INTO students (id, name, age, marks) VALUES (%s, %s, %s, %s)"

    values = (1, "Akansha", 22, 85)

    cursor.execute(sql, values)
    con.commit()

    print("Record inserted successfully!")

    cursor.close()
    con.close()

except mysql.connector.Error as e:
    print("Error:", e)
