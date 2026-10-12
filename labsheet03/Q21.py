# 21. Find the largest and smallest elements in a list. 


# Find the largest and smallest elements in a list

# Take input from the user
numbers = list(map(int, input("Enter list elements separated by spaces: ").split()))

# Check if the list is not empty
if len(numbers) > 0:
    largest = numbers[0]
    smallest = numbers[0]

    # Find largest and smallest elements
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    # Display the results
    print("Largest element:", largest)
    print("Smallest element:", smallest)
else:
    print("The list is empty.")