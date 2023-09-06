#Driving costs as a function of miles_per_gallon, 
#dollars_per_gallon, and miles_driven

def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    """Gas sure is expensive during war in Ukraine"""
    return miles_per_gallon * dollars_per_gallon * miles_driven


#Step counter, taking distance traveled in feet as input, and
#assuming 1 step = 2.5 feet

def step_counter(feet):
    """DOC."""
    if type(feet) == int or float:
        step = feet / 2.5
    return step


#Convert positive integer to base 2, represented by string of
#0s and 1s

def BaseConversion(N):
	# Stores the required answer
	s = ""
	# Iterate until N is
	# not equal to zero
	while (N != 0):

		# If N is Even
		if (N % 2 == 0):
			# Add char '0' in
			# front of string
			s = "0" + s
		else:
			# Add char '1' in
			# front of string
			s = "1" + s
			# Decrement N by 1
			N -= 1
		# Divide N by -2
		N /= -2
	# If string is empty,
	# that means N is zero
	if (s == ""):
		# Put '0' in string s
		s = "0"

	return s


#Return the nth element of the Fibonacci sequence, 0, 1, 1, 2,
#3, 5, 8, 13, where 0 is the 0th value

def fib(n):
    """DOC."""
    if n <3:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    return


#Integer checker: Is every character of string a digit 0–9?

def integer_checker(s):
    """DOC."""
    if type(s) ==str:
        return any(s.isdigit() for i in s)


#Names: first, middle, last in; last, first initial.middle init out.
def names(first, middle, last):
    """DOC."""
    if type(first) and type(middle) and type(last) == str:
        return str(last), str(first) + '.' + str(middle)


#Is string a palindrome (spaces do not count)
def isPalindrome(s):
    """DOC."""
    return s == s[::-1]


#Remove all non-alpha characters from string (hard closed book)
def alpha(s):
    """DOC."""
    if type(s) == str:
        result = ''.join(filter(str.isalnum, s))
    return result


#Input string of whitespace-separated numbers; output average (or max, etc.)
def sum_digits_string(str1):
    """DOC."""
    sum_digit = 0
    num = str1.split()
    print(type(num))
    count = len(num)
    for x in num:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z
            average = sum_digit / count
            maxval = max(num)
            minval = min(num)
    return sum_digit, average, maxval, minval


#Input list of integers; output list of nonnegative ones in sorted order
def ls(s):
    """DOC."""
    s.sort()
    result = list()
    for num in s:
        if num >=0:
            result.append(num)
    return result


#Input list of numbers, lower bound, and upper bound.
#Remove numbers not between lower & upper bounds.
def combo(ls, lower, upper):
    """DOC."""
    result = list()
    for num in ls:
        if ls.index(num)>=ls.index(lower) and ls.index(num) <= ls.index(upper):
            result.append(num)
    return result


#Given dictionary of item (type string), cost (type number)
#pairs, and list of strings, return sum of cost of items that are
#in the list and in the dictionary
def cost(d, item_ls):
    """Return s sum of costs of items in item_ls that are keys in d"""
    answer = 0
    for item in item_ls:
        if item in d:
            answer += d[item]
    return answer


#in_order: tells if list of numbers is in sorted order
def in_order(ls):
    """DOC."""
    new_ls = ls[:]
    new_ls.sort()
    if type(ls)== list:
        if ls == new_ls:
            return True
        else:
            return False
        
        
#Words in a range: inputs file name, lower and upper bound
#strings. File has one word per line. Return list of words that
#are alphabetically between lower and upper
def word_in_range(fname, lo, hi):
    """file fname has one word per line"""
    answer = []
    fname = '/Users/wondamonsta/Documents/for_python.rtf'
    with open(fname) as fref:
        words = fref.readlines()
    for w in words:
        wtrim = w[:-2] #because each word end with a newline \n (2 characters)
        if wtrim > lo and wtrim <= hi:
            answer.append(wtrim)
    return answer
            

#Build dictionary from file: input file name. File has 1 item per
#line, alternating between key and value. make the dictionary
def build_dict(fname):
    """DOC."""
    ls = list()
    with open(fname) as fref:
        words = fref.readlines()
    for word in words:
        ls.append(word)
    it = iter(ls)
    res_dct = dict(zip(it, it))
    return res_dct
    

#Half life decay: given initial value, half life, and amount of
#time (same units for half time and amount of time), return
#final amount. Assume partial time periods don't count
def decay(value, halflife, time):
    """DOC."""
    final_amount = [value*halflife**i for i in range(time)]
    return final_amount

#return longer of two input strings; second one if equal length
def check(s1, s2):
    """DOC."""
    if type(s1) == str and type(s2) == str:
        if len(s1) > len(s2):
            return s1
        elif len(s1) < len(s2):
            return s2
        else:
            return s2
    

#Length of string excluding spaces, periods, !s, commas
def clear(s):
    """DOC."""
    result = 0 #number of charachters
    count = 0 #to count index of user_text
    for i in s:
        if s[count] != ' ' and s[count] != '.' and s[count] != ',' and s[count] != '!':
            result += 1
        count += 1
    return result


#Two inputs: List of numbers and a number; change list to
#keep only entries below second input parameter
def lsmod(ls, num):
    """DOC."""
    ls.sort()
    result = list()
    for item in ls:
        if item<num:
            result.append(item)
    return result


#Count multiples: Three integers as input, lo, hi, x. Return
#number of multiples of x between lo & hi inclusive
def mult(lo, hi, x):
    """DOC."""
    count = 0
    if type(lo) == int and type(hi) == int and type(x) == int:
        for i in range(lo, hi+1):
            if i % x == 0:
                count+=1
    return count


#Hailstone sequence. Input positive integer x. Return list of
#hailstone sequence starting at x using rule that after entry n
#if n is even, next is n/2 and if n is odd, next is 3n+1. Stop at 1
def hailstone(x):
    """DOC."""
    result = list()
    result.append(int(x))
    if type(x) == int:
        while x != 1:
            if x%2 == 0:
                x = x/2
                result.append(int(x))
            else:
                x = 3*x + 1
                result.append(int(x))
    return result


#Inputs 3 integers. Output: input one w/largest absolute value
def positive(n1, n2, n3):
    """DOC."""
    if type(n1) == int and type(n2) == int and type(n3) == int:
        return max(abs(n1), abs(n2), abs(n3))

def pos1(n1, n2, n3):
    if type(n1) == int and type(n2) == int and type(n3) == int:
        if n1 <0 and n2 <0 and n3 <0:
            return max(-n1, -n2, -n3)
        else:
            return max(n1, n2, n3)
            

#Input positive integer. Output whether it's a leap year.
#Remember that for years divisible by 100, it's a leap year
#only if it's divisible by 400.
def leap(x):
    """DOC."""
    if type(x) == int and x>0:
        if x%400 ==0 and x%100 == 0:
            return True
        elif x%4 ==0 and x%100 != 0:
            return True
        else:
            return False


#Input: list of 3 nonnegative integers. Output: new list of 3
#integers, consisting of smallest from input list being
#subtracted from each of input list. e.g., input [130, 50, 111]
#gives output [80, 0, 61]
def almost(ls):
    """DOC."""
    result = list()
    minimum = list()
    if type(ls) == list:
        for i in ls:
            if i > 0:
                for i in ls:
                    x = min(ls)
                    minimum.append(x)
        for k in ls:
            value = k - minimum[0]
            result.append(value)
    return result


#Input: text string containing white space separated words,
#and a positive integer n. Output: List of lists of words, n
#words to a list, except last list can be shorter if total number
#of words not a multiple of n
def last(s, n):
    """DOC."""
    new = s.split(' ')
    copy = new[:]
    empty_list = list()
    for item in new:
        if len(new) > n:
            empty_list.append([]*(int(len(new)/n)))
    print(empty_list)
    print(new)
    result = list()
    new_res = list()
    if type(new) == list and type(n) == int and n > 0:
        #for i in copy:
            while len(copy)!=n-1:
            #while copy:
                result.append(copy.pop(0))
                print(copy)
            if len(copy) !=0:
                result.append(copy.pop(0))
    while copy:
        result.append([copy.pop()])
    #for i in result:
        #if i[i] %2 ==0 and i[i]%2 !=0:
            #new_res.append(list(i+i))
            
    return result
            
#a= ['a', 'b', 'c', 'd', 'e']
#b= []

#b.append(a.pop())
#b.append(a.pop())
#b.append(a.pop())

#print 'ListA =', a
#print 'ListB =', b
        

def last1(s,n):
    """DOC."""
    new = s.split(' ')
    num = (len(new)//n)
    print(new)
    print(num)
    result = list()
    print(result)
    for i in new:
        result.append(list(new.pop()))
        
        print(result)



#Rotate
def leftrotate(s,d):
    """DOC."""
    tmp = s[d:] + s[0:d]
    return tmp

def rightrotate(s,d):
    """DOC."""
    return leftrotate(s, len(s) - d)


def avg(x,y):
    """DOC."""
    return (x+y)/2

def count(s):
    """DOC."""
    count = 0
    for i in s:
        if i =='p' or i =='P':
            count+=1
        else:
            pass
    return count

def second(s):
    """DOC."""
    return s.count('p') + s.count('P')

            
def f(num):
    num = 4
    return 2

def g(val):
    num = 8
    print(f(1))

g(2)        
        
ls = [2, 4, 6, 8, 10]
b = [ ]
for item in ls:
    b.append(item+5)
print(b)
            
        

def lect(ls):
    """DOC."""
    new_ls = list()
    if type(ls) == list:
        for i in ls:
            if i < 0:
                new_ls.append(i)
            else:
                print('Try again')
    return sum(new_ls)


def new(ls):
    """DOC."""
    new_ls = list()
    if type(ls) == list:
        for i in ls:
            if i%2 == 0:
                new_ls.append(i)
            else:
                break
    return sum(new_ls)
            
                
                




        

    
        
    
    
    
    
    
    
    
    
    
    
    
    
    





















