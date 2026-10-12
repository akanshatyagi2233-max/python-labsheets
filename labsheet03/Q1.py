# Write a Python code to check if a string is a palindrome

text = input("enter a string:")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
