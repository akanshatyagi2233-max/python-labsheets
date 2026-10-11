p = float(input("enter loan amount:"))
r = float(input("enter interest rate:"))
n = int(input("enter tenure:"))

e = p*r*(1+r)**n / ((1+r)**n-1)

print("monthly EMI = ",e)