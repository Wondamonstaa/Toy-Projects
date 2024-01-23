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

