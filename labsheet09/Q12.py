import mysql.connector

# Connect to database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="akansha07",
    database="college"
)

cur = con.cursor()

# Insert student record
sql = "INSERT INTO students (id, name, age, marks) VALUES (%s, %s, %s, %s)"

data = (101, "Akansha", 22, 85)

cur.execute(sql, data)
con.commit()

print("Student record inserted successfully!")

cur.close()
con.close()
