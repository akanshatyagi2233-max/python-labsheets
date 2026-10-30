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
        CREATE TABLE IF NOT EXISTS temp_students (
            id INT,
            name VARCHAR(50)
        )
    """)

    cursor.execute("INSERT INTO temp_students VALUES (1, 'Test')")
    
    cursor.execute("TRUNCATE TABLE temp_students")

    print("Table truncated successfully!")

    cursor.close()
    con.close()

except mysql.connector.Error as e:
    print("Error:", e)
