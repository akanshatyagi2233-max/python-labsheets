# 28. Find common elements in two lists. 

# Python program to find common elements in two lists

# Take input for the first list dynamically
input1 = input("Enter elements for the first list (separated by space): ")
list1 = list(map(int, input1.split()))

# Take input for the second list dynamically
input2 = input("Enter elements for the second list (separated by space): ")
list2 = list(map(int, input2.split()))

# Find common elements using set intersection (& operator)
# set() helps to remove any duplicate values during comparison
common_elements = list(set(list1) & set(list2))

# Display the results in a user-friendly format
print("\n--- Results ---")
print("First List:", list1)
print("Second List:", list2)
print("Common Elements:", common_elements)
