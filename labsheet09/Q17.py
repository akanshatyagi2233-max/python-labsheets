import mysql.connector

# Connect to database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="akansha07",
    database="college"
)

cur = con.cursor()

# Count total records
cur.execute("SELECT COUNT(*) FROM students")

result = cur.fetchone()

print("Total number of students:", result[0])

cur.close()
con.close()

