# 8. Convert a string into title case without using built-in functions. 

string = input("enter a string:")
result = ""
new_word = True
for i in string:
    if i == " ":
        result += i
        new_word = True
    elif new_word:
     result+=i.upper()
     new_word = False
    else:
     result += i
print("title case:",result)
        
