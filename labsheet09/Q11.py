import mysql.connector

# Connect to MySQL database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="akansha07",
    database="college"
)

# Create cursor
cur = con.cursor()

# Create students table
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    marks FLOAT
)
""")

print("Students table created successfully!")

# Close connection
cur.close()
con.close()
