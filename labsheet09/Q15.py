import mysql.connector

# Connect to database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="akansha07",
    database="college"
)

cur = con.cursor()

# Update student marks
roll = int(input("Enter student roll number: "))
marks = float(input("Enter new marks: "))

cur.execute(
    "UPDATE students SET marks = %s WHERE id = %s",
    (marks, roll)
)

con.commit()

if cur.rowcount > 0:
    print("Student marks updated successfully!")
else:
    print("Student not found or marks unchanged")

cur.close()
con.close()
