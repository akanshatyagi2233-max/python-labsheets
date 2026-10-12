# 14. Merge two dictionaries into one. 

# Create two dictionaries
dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}

# Merge two dictionaries
dict3 = dict1.copy()
dict3.update(dict2)

# Display the merged dictionary
print("Merged Dictionary:", dict3)