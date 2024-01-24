#Cartesian product
from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

#Unpacks the list of tuples using *
print(*list(product(a, b)))

#Itertools.permutations()
from itertools import permutations

string, size = input().split()

# Get the sorted permutations
sorted_perms = sorted(permutations(string, int(size)))

# Print each permutation on a separate line
for perm in sorted_perms:
    print(''.join(perm))


#Combinations
from itertools import combinations

s, k = input().split()
letters = sorted(s)

#Combinations with replacement
from itertools import combinations_with_replacement as cwr

S, k = input().split()

print("\n".join(["".join(e) for e in cwr(sorted(S), int(k))]))

for i in range(1, int(k) + 1):
    for combination in combinations(letters, i):
        print("".join(combination))

#Groupby
from itertools import groupby
from collections import Counter

string = input()

groups = groupby(string)
counter = Counter()

result = []

for k, v in groups:
    result.append((len(list(v)), int(k)))

print(*result)
