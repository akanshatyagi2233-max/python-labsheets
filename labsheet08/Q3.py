
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
        CREATE TABLE IF NOT EXISTS students (
            id INT PRIMARY KEY,
            name VARCHAR(50),
            age INT,
            marks FLOAT
        )
    """)

    print("Students table created successfully!")

    cursor.close()
    con.close()

except mysql.connector.Error as e:
    print("Error:", e)