students = [
    {"roll": 1, "name": "Akansha", "marks": 85},
    {"roll": 2, "name": "Juhi", "marks": 78}
]

roll = int(input("Enter roll number: "))

for student in students:
    if student["roll"] == roll:
        marks = float(input("Enter new marks: "))
        student["marks"] = marks
        print("Marks updated successfully!")
        break
else:
    print("Student not found")

print(students)
