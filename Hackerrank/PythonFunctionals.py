#Fibonacci and Lambdas
cube = lambda x: pow(x, 3)

def fibonacci(n):
    
    if n == 1:
        return [0]
    
    x, y, lst = 0, 1, []
    for _ in range(n):
        lst.append(x)
        x, y = y, x + y
    return lst

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

#Regex
import re
def fun(s):
    return re.search(r'^[a-zA-Z0-9_-] + @[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s)
    

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)


#Reduce
from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x*y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
