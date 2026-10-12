# 3. Remove all negative numbers from a list. 

# Input list
numbers = [10, -5, 20, -3, 0, 15, -8]

# Remove negative numbers
positive_numbers = [num for num in numbers if num >= 0]

# Display result
print("Original list:", numbers)
print("List after removing negative numbers:", positive_numbers)