# 29. Find common keys between two dictionaries. 

# Two dictionaries
dict1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
dict2 = {'b': 50, 'c': 60, 'e': 70}

# Find common keys
common_keys = dict1.keys() & dict2.keys()

# Display the result
print("Common keys:", common_keys)