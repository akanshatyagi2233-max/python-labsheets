p= float(input("enter principal:"))
r= float(input("enter rate :"))
t = int(input("enter time :"))

a = p*(1+r/100)**t
ci = a-p
print(' compound interest = ',ci)







