
import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="akansha07",
        database="student_db"
    )

    if con.is_connected():
        print("Database Connected Successfully!")

    con.close()

except mysql.connector.Error as e:
    print("Error:", e)