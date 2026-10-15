t1 = (10, 20, 30, 40)
t2 = (30, 40, 50, 60)

difference = tuple(x for x in t1 if x not in t2)

print("Difference:", difference)
