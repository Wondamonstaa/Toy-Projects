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
