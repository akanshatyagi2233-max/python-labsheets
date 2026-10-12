# 27. Find the second largest number in a list. 

# Python program to find the second largest number in a list

# Take input for the list dynamically
user_input = input("Enter elements for the list (separated by space): ")
numbers = list(map(int, user_input.split()))

# Check if the list has at least 2 elements
if len(numbers) < 2:
    print("The list must contain at least 2 elements to find the second largest number.")
else:
    # Remove duplicate values using set and sort them in descending order
    unique_numbers = sorted(list(set(numbers)), reverse=True)
    
    # Check if there are at least two unique elements
    if len(unique_numbers) < 2:
        print("All elements in the list are identical. There is no distinct second largest number.")
    else:
        second_largest = unique_numbers[1]
        
        # Display the results in a user-friendly format
        print("\n--- Results ---")
        print("Original List:", numbers)
        print("Second Largest Number:", second_largest)
