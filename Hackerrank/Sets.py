n, m = (int(i) for i in input().split(' '))

S = [int(i) for i in input().split(' ')]

A = set([int(i) for i in input().split(' ')])
B = set([int(i) for i in input().split(' ')])

#C = set([int(i) for i in input().split(' ')]) list comprehension
#D = set([int(i) for i in input().split(' ')])
print(sum((1 for i in S if i in A)) - sum((1 for i in S if i in B)))



#Add and count the number of elements
print(len(set([input() for i in range(int(input()))])))


#Set operations
R = int(input())
S = set(map(int, input().split()))
M = int(input())

for _ in range(M):
    command, *args = input().split()
    if command == "remove":
        S.remove(int(args[0]))
    elif command == "discard":
        S.discard(int(args[0]))
    elif command == "pop":
        S.pop()
print(sum(S))


#UNION
try:
    
    a = int(input())
    if a < 1000:
        s1 = set(map(int, input().split(' ')))
    
    b = int(input())
    if b < 1000:
        s2 = set(map(int, input().split(' ')))
    
    print(len(s1.union(s2)))
    
except ValueError:
    print("Incorrect bounds!")


#INTERSECTION
try:

    a = int(input())
    if a < 1000:
        s1 = set(map(int, input().split(' ')))
    
    b = int(input())
    if b < 1000:
        s2 = set(map(int, input().split(' ')))
    
    print(len(s1.intersection(s2)))
    
except ValueError:
    print("Incorrect bounds!")


#DIFFERENCE
try:

    a = int(input())
    if a < 1000:
        s1 = set(map(int, input().split(' ')))
    
    b = int(input())
    if b < 1000:
        s2 = set(map(int, input().split(' ')))
    
    print(len(s1.difference(s2)))
    
except ValueError:
    print("Incorrect bounds!")


#SYMMETRIC DIFFERENCE
try:

    a = int(input())
    if a < 1000:
        s1 = set(map(int, input().split(' ')))
    
    b = int(input())
    if b < 1000:
        s2 = set(map(int, input().split(' ')))
    
    print(len(s1.symmetric_difference(s2)))
    
except ValueError:
    print("Incorrect bounds!")


#Combination of set methods 
# Enter your code here. Read input from STDIN. Print output to STDOUT

number = int(input())

a = set(map(int, input().split(' ')))

other = int(input())

methods = {
    "update": "update",
    "intersection_update": "intersection_update",
    "difference_update": "difference_update",
    "symmetric_difference_update": "symmetric_difference_update"
}

for _ in range(other):
    
    head, *tail = input().split(' ')
    
    s = set(map(int, input().split(' ')))

    getattr(a, methods[head])(s)
    

print(sum(a))

#Collections Counter
from collections import Counter

# Size of each group
group_size = int(input())

# Unordered elements of the room number list
room_number_list = input().split(' ')

answer = 0

try:
    if group_size > 1:
        
        counter = Counter(room_number_list)
        
        least_common_element, lowest_count = counter.most_common()[-1]
        
        answer = least_common_element
        
    print(answer)
    
except ValueError:
    
    print("Size <= 1")

