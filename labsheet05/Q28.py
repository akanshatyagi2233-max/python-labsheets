t = (10, 20, 30, 10, 40, 20, 50)

repeated = tuple(x for x in set(t) if t.count(x) > 1)

print("Repeated items:", repeated)
