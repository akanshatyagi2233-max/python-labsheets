# 17. Print all substrings of a string. 

s = input("Enter a string: ")

print("All substrings are:")

# Generate all possible substrings
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        print(s[i:j])
