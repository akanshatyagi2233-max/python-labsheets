# 13. Convert all vowels in a string to uppercase and consonants to lowercase. 

s = input("Enter a string: ")
result = ""

for ch in s:
    if ch.lower() in "aeiou":
        result += ch.upper()
    else:
        result += ch.lower()

print(result)