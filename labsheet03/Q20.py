# 20. Check if two strings are rotations of each other. 

# Check if two strings are rotations of each other

# Take input from the user
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

# Check whether the strings are rotations
if len(s1) == len(s2) and s2 in (s1 + s1):
    print("The strings are rotations of each other.")
else:
    print("The strings are not rotations of each other.")
