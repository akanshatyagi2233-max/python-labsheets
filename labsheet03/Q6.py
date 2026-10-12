# 6. Find the frequency of each character in a string. 

string = input("Enter a string:")
result = ""

for i in string:
    if i not in result:
        print(i,":",string.count(i))
        result += i
