
# 5. Remove all duplicate characters from a string. 

string = input("enter a string:")
result = ""

for i in string:
    if i not in result:
        result += i

print("string after removing duplicates:",result)
