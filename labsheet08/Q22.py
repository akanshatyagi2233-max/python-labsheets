import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="akansha07",
        database="student_db"
    )

    cursor = con.cursor()

    query = """
    SELECT students.name, courses.course_name
    FROM students
    INNER JOIN courses
    ON students.id = courses.course_id
    """

    cursor.execute(query)

    records = cursor.fetchall()

    for row in records:
        print(row)

    cursor.close()
    con.close()

except mysql.connector.Error as e:
    print("Error:", e)
