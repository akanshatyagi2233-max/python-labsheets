# 22. Sort a list of integers in ascending and descending order. 

# Sort a list in ascending and descending order

# Take input from the user
numbers = list(map(int, input("Enter list elements separated by spaces: ").split()))

# Sort in ascending order
ascending = sorted(numbers)

# Sort in descending order
descending = sorted(numbers, reverse=True)

# Display the results
print("Ascending order:", ascending)
print("Descending order:", descending)
