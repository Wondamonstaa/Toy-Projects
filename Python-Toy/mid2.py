#Question 5 Mid 2

ex_ls = [1,2,3,4,5]
"""Remove the LAST item from the list."""
ex_ls.pop()
"""Give the num of element in the list."""
len(ex_ls)


#Question 6 Mid 2
def modify(names, score):
    names.append('Robert')
    score = score + 20
    
players = ['James', 'Tanya', 'Roxanne']
score = 150
modify(players, score)
print(players)


#Question 12 Mid 2
number = 70
guess = 55
while number != guess:
    if number > guess:
        guess = guess + 10
    else:
        guess = guess - 1
    print("The number is:", guess)

"""Byte = a group of binary digits 0-1, consists of bits."""
#Question 16 Mid 2
z = 0
a = 5
while a > 0:
    a = a -1
    if a == 2:
        continue
    z = z + a
    

#Question 17 Mid 2
my_list = [ 3, 2, 7, 8, 6, 9 ]
count = 0
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i-1]:
        count = count + 1
print(count)


#Question 19 Mid 2 part a
def fact(a):
    """DOC."""
    result = 1
    if type(a) == int and a >= 1:
        for i in range(1, int(a)+1):
            result *= i
    return result

def factorial(num):
    """Calculates and returns the factorial (num!)"""
    x = 1
    for i in range(1, num + 1):
        x *= i

    return x


#n = input("Enter a number: ")
#factorial = 1
#if int(n) >= 1:
#for i in range (1,int(n)+1):
#   factorial = factorial * i
#print("Factorail of ",n , " is : ",factorial)


#Question 19 Mid 2 part b
def long_count(ls, n):
    """DOC."""
    count = 0
    new_ls = list()
    if type(ls) == list and type(n) == int and n>=1:
        for item in ls:
            if len(item) == n:
                count +=1
                new_ls.append(item)
    return count, new_ls
                
        
ls = [[4, [True, False], 6, 8], [28, 9]] 
if ls[0][1][0]:
    print(ls[1][0])
else:
    print(ls[1][1])
    
    
    
#Mid 1 Functions
    
def average(s, i):
    """DOC."""
    if type(s) == int or float and type(i) == int or float:
        result = (s + i)/2
    return result
        

def dog_test(n):
    """DOC."""
    target = 'd' or 'o' or 'g'
    if type(n) == str:
        if n.find(target) != -1:
            return True
        else:
            return False
    else:
        return False
    return
    

def p_count(s):
    """DOC."""
    #count = 0
    if type(s) == str:
       result = s.count('p') + s.count('P')
    else:
        False
    return int(result)


#Fibonacci
def fib(n):
    """DOC."""
    if n <3:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    return

#Hailstone
def hailstone(n):
  hailstone_list = []
  hailstone_list.append(int(n))
  while n != 1:
    if n % 2 == 0:
      n = n/2
      hailstone_list.append(int(n))
    else:
      n = 3*n + 1
      hailstone_list.append(int(n))
  return hailstone_list
