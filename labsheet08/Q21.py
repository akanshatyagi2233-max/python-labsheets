
import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="akansha07",
        database="student_db"
    )

    cursor = con.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            course_id INT PRIMARY KEY,
            course_name VARCHAR(50)
        )
    """)

    sql = "INSERT IGNORE INTO courses (course_id, course_name) VALUES (%s, %s)"

    values = [
        (101, "Python"),
        (102, "DBMS"),
        (103, "Web Designing")
    ]

    cursor.executemany(sql, values)
    con.commit()

    print("Courses table created and data inserted successfully!")

    cursor.close()
    con.close()

except mysql.connector.Error as e:
    print("Error:", e)