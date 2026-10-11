a = int(input("enter first number:"))
b = int(input("enter second number:"))
lcm = max(a,b)

while lcm %a != 0 or lcm % b != 0 :
    lcm = lcm +1
print(lcm)

