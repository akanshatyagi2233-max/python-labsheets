marks = int(input("enter your marks"))

if marks>=90 and marks<=100:
    print("A grade:")
elif marks>=75 and marks<=89:
    print("B grade:")
elif marks>=50 and marks<=74:
    print("C grade:")
elif marks>50:
    print("D grade:")
else:
    print("fail:")

