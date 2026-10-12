# 14. Remove all punctuation from a string. 

import string

s = input("Enter a string: ")
result = ""

for ch in s:
    if ch not in string.punctuation:
        result += ch

print(result)
