import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="akansha07"
    )

    cursor = con.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS college_db")

    print("Database created successfully!")

    cursor.close()
    con.close()

except mysql.connector.Error as e:
    print("Error:", e)
