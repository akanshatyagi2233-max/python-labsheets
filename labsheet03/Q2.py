# 2. Count the number of vowels and consonants in a string. 

string = input("enter a string:")
countvowel = 0
countconsonats=0
for i in string:
 if i in "aeiouAEIOU":
    countvowel+=1
 else:
   countconsonats+=1

print("number of vowels = ",countvowel)
print("number of consonants = ",countconsonats)

