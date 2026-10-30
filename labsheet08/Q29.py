import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="akansha07",
        database="student_db"
    )

def insert_student(id, name, age, marks):
    con = connect_db()
    cursor = con.cursor()

    query = """
    INSERT INTO students (id, name, age, marks)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (id, name, age, marks))
    con.commit()

    print("Student inserted successfully!")

    cursor.close()
    con.close()

def fetch_students():
    con = connect_db()
    cursor = con.cursor()

    cursor.execute("SELECT * FROM students")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    con.close()

try:
    insert_student(5, "Rahul", 22, 82)
    print("\nStudent Records:")
    fetch_students()

except mysql.connector.Error as e:
    print("Database Error:", e)
