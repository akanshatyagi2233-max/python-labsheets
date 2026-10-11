# fibbonaci series

n = int(input("enter number of terms:"))
a =0
b= 1
sum = 0

for i in range(n):
    print(a,end=" ")
    sum = sum+a
    a,b = b,a+b

mean = sum/n
print("mean = ",mean )
print("sum of the series = ",sum)

