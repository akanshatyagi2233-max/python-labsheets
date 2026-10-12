# 29. Find the difference between two lists. 

# Python program to find the difference between two lists (List 1 - List 2)

# Take input for the first list dynamically
input1 = input("Enter elements for the first list (separated by space): ")
list1 = list(map(int, input1.split()))

# Take input for the second list dynamically
input2 = input("Enter elements for the second list (separated by space): ")
list2 = list(map(int, input2.split()))

# Find the difference using set subtraction (-)
# This filters out elements of list1 that are present in list2
difference_elements = list(set(list1) - set(list2))

# Display the results in a user-friendly format
print("\n--- Results ---")
print("First List:", list1)
print("Second List:", list2)
print("Difference (List 1 - List 2):", difference_elements)
