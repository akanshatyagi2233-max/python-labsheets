import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="akansha07",
        database="student_db"
    )

    cursor = con.cursor()

    cursor.execute("SHOW TABLES LIKE 'students'")

    result = cursor.fetchone()

    if result:
        print("Students table exists!")
    else:
        print("Students table does not exist!")

    cursor.close()
    con.close()

except mysql.connector.Error as e:
    print("Error:", e)                                                                                                                                                      
