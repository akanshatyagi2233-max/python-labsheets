# 24. Reverse a list without using built-in functions. 

# Reverse a list without using built-in functions

# Take input from the user
numbers = list(map(int, input("Enter list elements separated by spaces: ").split()))

# Reverse the list using a loop
reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

# Display the reversed list
print("Reversed list:", reversed_list)
