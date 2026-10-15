t = ((10, 20), (30, 40), (50, 60))

flat_tuple = tuple(item for subtuple in t for item in subtuple)

print("Flattened tuple:", flat_tuple)
