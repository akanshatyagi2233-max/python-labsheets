# Write student data into file

with open("students.txt", "w") as file:
    file.write("1, Akansha, 85\n")
    file.write("2, Juhi, 78\n")

print("Data saved successfully!")

# Read student data

with open("students.txt", "r") as file:
    print(file.read())
