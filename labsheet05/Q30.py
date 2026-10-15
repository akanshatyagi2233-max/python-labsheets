t1 = (10, 20, 30)
t2 = (40, 50, 60)

result = tuple(a + b for a, b in zip(t1, t2))

print("Element-wise sum:", result)
