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

    values = [
        (2, "Juhi", 22, 78),
        (3, "Shristi", 21, 90),
        (4, "Ayushi", 23, 88)
    ]

    cursor.executemany(sql, values)
    con.commit()

    print(cursor.rowcount, "Records inserted successfully!")

    cursor.close()
    con.close()

except mysql.connector.Error as e:
    print("Error:", e)
