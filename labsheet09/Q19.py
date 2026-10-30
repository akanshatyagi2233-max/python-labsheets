import mysql.connector

# Connect to database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="akansha07",
    database="college"
)

cur = con.cursor()

# Find student with highest marks
cur.execute("""
SELECT * FROM students
ORDER BY marks DESC
LIMIT 1
""")

student = cur.fetchone()

if student:
    print("Student with highest marks:", student)
else:
    print("No student records found")

cur.close()
con.close()
