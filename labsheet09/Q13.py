import mysql.connector

# Connect to database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="akansha07",
    database="college"
)

cur = con.cursor()

# Display all student records
cur.execute("SELECT * FROM students")

records = cur.fetchall()

print("Student Records:")

for row in records:
    print(row)

cur.close()
con.close()
