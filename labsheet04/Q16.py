# 16. Sort a dictionary by values. 

# Original dictionary
my_dict = {'a': 4, 'b': 1, 'c': 3, 'd': 2}

# Sort dictionary by values
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Display the sorted dictionary
print("Sorted dictionary:", sorted_dict)