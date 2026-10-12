# 12. Find the maximum and minimum marks from a dictionary. 

# Dictionary of student names and marks
students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Neha": 88
}

# Find maximum and minimum marks
maximum = max(students.values())
minimum = min(students.values())

print("Maximum marks:", maximum)
print("Minimum marks:", minimum)