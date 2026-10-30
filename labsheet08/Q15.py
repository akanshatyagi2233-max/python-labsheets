import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="akansha07",
        database="student_db"
    )

    cursor = con.cursor()

    cursor.execute(
        "SELECT * FROM students ORDER BY marks DESC LIMIT 3"
    )

    records = cursor.fetchall()

    for row in records:
        print(row)

    cursor.close()
    con.close()

except mysql.connector.Error as e:
    print("Error:", e)
