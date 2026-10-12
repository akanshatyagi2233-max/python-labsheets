# 23. Remove duplicate elements from a list. 

# Remove duplicate elements from a list

# Take input from the user
numbers = list(map(int, input("Enter list elements separated by spaces: ").split()))

# Create an empty list to store unique elements
unique_list = []

# Check and remove duplicates
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

# Display the result
print("List after removing duplicates:", unique_list)
