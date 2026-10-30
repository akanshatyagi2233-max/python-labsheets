import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="akansha07",
        database="student_db"
    )

    cursor = con.cursor()

    # Intentionally incorrect query to demonstrate error handling
    cursor.execute("SELECT * FROM wrong_table")

except mysql.connector.Error as e:
    print("Database Error:", e)

finally:
    if 'cursor' in locals():
        cursor.close()

    if 'con' in locals() and con.is_connected():
        con.close()
