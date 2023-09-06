
import re
string = "Hello, Mr. John. Have a good day."
print(len("".join(re.findall(r'[A-Z0-9a-z]', string))) ) 


def cost(d, item_ls):
    """Return a sum of costs of items in item_ls that are key in d"""
    answer = 0
    for item in item_ls:
        if item in d:
            answer += d[item]
    return answer


def word_in_range(fname, lo, hi):
    """file fname has one word per line"""
    answer = list()
    with open(fname) as fref:
        words = fref.readlines()
    for w in words:
        wtrim = w[:-2]
        if wtrim > lo and wtrim <= hi:
            answer.append(wtrim)
    return answer


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



def char_count(s, target):
    """DOC."""
    new_str = s.split()
    if type(new_str) == list:
        for i in new_str:
            if target in new_str:
                return len(target)
            else:
                return 0
        else:
            print('try again')
    return