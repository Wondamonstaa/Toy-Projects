n, m = (int(i) for i in input().split(' '))

S = [int(i) for i in input().split(' ')]

A = set([int(i) for i in input().split(' ')])
B = set([int(i) for i in input().split(' ')])

#C = set([int(i) for i in input().split(' ')]) list comprehension
#D = set([int(i) for i in input().split(' ')])
print(sum((1 for i in S if i in A)) - sum((1 for i in S if i in B)))



#Add and count the number of elements
print(len(set([input() for i in range(int(input()))])))
