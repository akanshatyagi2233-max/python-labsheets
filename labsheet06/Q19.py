
from itertools import chain, combinations

s = {1, 2, 3}

power_set = chain.from_iterable(
    combinations(s, r) for r in range(len(s) + 1)
)

print("Power set:")
for subset in power_set:
    print(set(subset))