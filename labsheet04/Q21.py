# 21. Find the key with the maximum value in a dictionary. 

# Original dictionary
my_dict = {'a': 10, 'b': 50, 'c': 30, 'd': 20}

# Find the key with the maximum value
max_key = max(my_dict, key=my_dict.get)

# Display the result
print("Key with maximum value:", max_key)
print("Maximum value:", my_dict[max_key])