# 7. Reverse a string without using slicing. 

string = input("enter a string:")
reverse = ""

for i in string:
    reverse = i + reverse
print("reverse string = ",reverse)


#    Second Method

# new= string[::-1]
# print("Reverse string= ",new)
