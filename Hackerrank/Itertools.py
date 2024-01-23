#Cartesian product
from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

#Unpacks the list of tuples using *
print(*list(product(a, b)))
