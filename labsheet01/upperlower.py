ch = input("enter a character:")

if ch.isupper():
    print("upper case")
elif ch.islower():
    print("lower case")
elif ch.isdigit():
    print("digit")
else:
    print("special character")
