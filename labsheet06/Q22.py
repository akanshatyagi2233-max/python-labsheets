my_list = [10, 20, 10, 30, 20, 40]

seen = set()
duplicates = set()

for x in my_list:
    if x in seen:
        duplicates.add(x)
    else:
        seen.add(x)

print("Duplicate elements:", duplicates)
