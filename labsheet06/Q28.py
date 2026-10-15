s = frozenset([10, 20, 30, 40])

print("Frozen set:", s)
print("Length:", len(s))
print("Is 20 present?", 20 in s)

# Frozen sets are immutable
print("Union:", s.union({50, 60}))
