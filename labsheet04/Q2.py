# 2. Rotate a list by n positions. 

# Input list
numbers = [1, 2, 3, 4, 5]

# Number of positions to rotate
n = 2

# Rotate the list to the right
n = n % len(numbers)
rotated = numbers[-n:] + numbers[:-n]

# Display result
print("Original list:", numbers)
print("Rotated list:", rotated)