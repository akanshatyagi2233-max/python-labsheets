# 24. Invert a dictionary (keys become values and values become keys). 

# Original dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Invert the dictionary
inverted_dict = {value: key for key, value in my_dict.items()}

# Display the inverted dictionary
print("Inverted dictionary:", inverted_dict)