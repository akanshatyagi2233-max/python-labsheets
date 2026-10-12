# 26. Merge two lists into one. 

# Python program to merge two lists into one

# Take input for the first list dynamically
input1 = input("Enter elements for the first list (separated by space): ")
list1 = list(map(int, input1.split()))

# Take input for the second list dynamically
input2 = input("Enter elements for the second list (separated by space): ")
list2 = list(map(int, input2.split()))

# Merge the two lists using the '+' operator
merged_list = list1 + list2

# Display the results in a user-friendly format
print("\n--- Results ---")
print("First List:", list1)
print("Second List:", list2)
print("Merged List:", merged_list)
