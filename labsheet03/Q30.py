# 30. Separate even and odd numbers from a list. 

# Python program to separate even and odd numbers from a list

# Take input for the list dynamically
user_input = input("Enter elements for the list (separated by space): ")
numbers = list(map(int, user_input.split()))

# Initialize empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Loop through each number and classify it
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Display the results in a user-friendly format
print("\n--- Results ---")
print("Original List:", numbers)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
