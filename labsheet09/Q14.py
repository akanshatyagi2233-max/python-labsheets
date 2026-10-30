import mysql.connector

# Connect to database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="akansha07",
    database="college"
)

cur = con.cursor()

# Search student by roll number
roll = int(input("Enter student roll number: "))

cur.execute(
    "SELECT * FROM students WHERE id = %s",
    (roll,)
)

record = cur.fetchone()

if record:
    print("Student Found:", record)
else:
    print("Student not found")

cur.close()
con.close()
