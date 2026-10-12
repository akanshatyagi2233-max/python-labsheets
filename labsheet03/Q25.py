# 25. Count the frequency of each element in a list. 

# Count the frequency of each element in a list

# Take input from the user
numbers = list(map(int, input("Enter list elements separated by spaces: ").split()))

# Create an empty dictionary
frequency = {}

# Count the frequency of each element
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Display the frequency
print("Frequency of each element:")
for num in frequency:
    print(num, ":", frequency[num])
