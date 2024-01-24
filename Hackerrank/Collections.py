from collections import Counter

shoes = int(input())
shoes_sizes = [x for x in input().split(' ')]

customers = int(input())
counter = Counter(shoes_sizes)

answer = 0

for i in range(customers):
    customer_input = input().split(' ')
    size = customer_input[0]
    amount = int(customer_input[1])

    if counter[size] >= 1:
        answer += amount
        counter[size] -= 1  # Decrement the count for the purchased size

print(answer)

#Default dict
from collections import defaultdict
N, M = map(int, input().split())

A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

d = defaultdict(list)

for index, item in enumerate(A):
    d[item].append(index+1)

for item in B:
    if item in A:
        print(*d[item])
    else:
        print(-1)

#Namedtuple
from collections import namedtuple

N = int(input())
Names = namedtuple('Names', input().split())

print(sum([int(Names(*list(map(str, input().split()))).MARKS) for _ in range(N)])/N)
