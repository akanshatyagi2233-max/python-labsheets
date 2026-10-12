# 27. Remove duplicate values from a dictionary. 


# Original dictionary
my_dict = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}

# Remove duplicate values
unique_dict = {}
seen_values = set()

for key, value in my_dict.items():
    if value not in seen_values:
        unique_dict[key] = value
        seen_values.add(value)

# Display the dictionary
print("Dictionary after removing duplicates:", unique_dict)