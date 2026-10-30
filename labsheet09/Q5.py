students = [
    {"roll": 1, "name": "Akansha", "marks": 85},
    {"roll": 2, "name": "Juhi", "marks": 78}
]

roll = int(input("Enter roll number to delete: "))

for student in students:
    if student["roll"] == roll:
        students.remove(student)
        print("Student deleted successfully!")
        break
else:
    print("Student not found")

print(students)
