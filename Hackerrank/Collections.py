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

#Namedtuple detailed
from collections import namedtuple

N = int(input())

Names = namedtuple('Names', input().split())

#List comprehension: accept items of type string via input, add them to the list, unpack the list, extracts the "MARKS" field from the named tuple and convert it to an integer
#Finally, iterate within the range N for each student, then calculate the sum of the MARKS column, divide by N, and print the result
marks = [int(Names(*list(input().split())).MARKS) for _ in range(N)]

result = sum(marks) / N

print(result)


#Ordered Dictionary
from collections import OrderedDict

od = OrderedDict()

N = int(input())

for i in range(N):
    
    parts = input().split()
    item_name = ' '.join(parts[:-1])  # Join all elements except the last one as item_name
    item_price = int(parts[-1])  # The last element is the price

    # If the item_name is already in the dictionary, update the item_price
    if item_name in od:
        od[item_name] += item_price
    else:
        od[item_name] = item_price

for item_name, item_price in od.items():
    print(item_name, item_price)

#Deque
from collections import deque

d = deque()

N = int(input())

methods = {
    "append": "d.append",
    "pop": "d.pop",
    "appendleft": "d.appendleft",
    "popleft": "d.popleft"
}

for i in range(N):
    command = input().split()
    method = command[0]
    
    if method in methods:
        eval(methods[method])(*command[1:])


print(*d)
