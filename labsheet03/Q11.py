# 11. Check if two strings are anagrams of each other. 

s1 = input("enter string 1:")
s2 = input("enter string 2")
a = sorted(s1)
b = sorted(s2)

if a==b:
    print("Anagram")
else:
    print("Not Anagram")