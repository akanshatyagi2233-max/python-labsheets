# 4. Extract all uppercase characters from a string. 

string = input("enter a string:")
for i in string:
    if i.isupper():
        print(i)
