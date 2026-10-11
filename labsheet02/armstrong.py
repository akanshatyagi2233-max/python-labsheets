n = int (input("enter a number:"))

temp = n
sum = 0

while n>0:
    digit = n%10
    sum = sum+ digit**3
    n = n//10

    if temp==n:
        print("armstorng number")
else:
    print("not a armstrong number")
    
