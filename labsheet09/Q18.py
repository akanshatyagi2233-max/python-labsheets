import mysql.connector

# Connect to database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="akansha07",
    database="college"
)

cur = con.cursor()

# Sort students by name
cur.execute("SELECT * FROM students ORDER BY name ASC")

records = cur.fetchall()

print("Student Records in Alphabetical Order:")

for row in records:
    print(row)

cur.close()
con.close()
