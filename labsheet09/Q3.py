students = [
    {"roll": 1, "name": "Akansha", "marks": 85},
    {"roll": 2, "name": "Juhi", "marks": 78}
]

name = input("Enter student name to search: ")

found = False

for student in students:
    if student["name"].lower() == name.lower():
        print("Student Found:", student)
        found = True
        break

if not found:
    print("Student not found")
