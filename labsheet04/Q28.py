# 28. Create a nested dictionary for student details (Name, Roll, Marks). 

# Create a nested dictionary
students = {
    1: {
        'Name': 'Rahul',
        'Roll': 101,
        'Marks': 85
    },
    2: {
        'Name': 'Priya',
        'Roll': 102,
        'Marks': 92
    },
    3: {
        'Name': 'Amit',
        'Roll': 103,
        'Marks': 78
    }
}

# Display student details
print("Student Details:")

for student_id, details in students.items():
    print("Student ID:", student_id)
    print("Name:", details['Name'])
    print("Roll:", details['Roll'])
    print("Marks:", details['Marks'])
    print()