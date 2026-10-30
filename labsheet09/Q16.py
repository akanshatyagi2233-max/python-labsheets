import mysql.connector

# Connect to database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="akansha07",
    database="college"
)

cur = con.cursor()

# Delete student record
roll = int(input("Enter student roll number: "))

cur.execute(
    "DELETE FROM students WHERE id = %s",
    (roll,)
)

con.commit()

if cur.rowcount > 0:
    print("Student record deleted successfully!")
else:
    print("Student not found")

cur.close()
con.close()
