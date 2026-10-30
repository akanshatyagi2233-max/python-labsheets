# Create a list of student records

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    roll = int(input("Enter roll number: "))
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }

    students.append(student)

print("\nStudent records created successfully!")
print(students)
