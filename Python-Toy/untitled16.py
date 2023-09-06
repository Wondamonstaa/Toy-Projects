#Name: Kiryl Baravikou
#Course: CS113
#Date: 4/26/22
#Project 7: 

    
#Write a function build_dictionary() 
#that takes as input a list of of strings, 
#ex. ['tomato', 'cucumber', 'celery'], 
#that is intended to be a list of words. 
#The function should return a dictionary 
#whose keys are every word that occurs in the list, 
#and whose values are the frequency of each word in the list.

def build_dictionary(s):
    """The build(s) function takes one string 's' as input and returns a dictionary."""
    keys = list()
    values = list()
    result = dict()
    #filter(lambda ls: type(list(str)) in ls,s)
    
    if s == list:
        for key in s:
            if key in s == str:
                keys.append(key)
            else:
                print('Please, enter a list of strings!')
        for word in keys:
            if word in s == str:
                result = word.count()
                values.append(result)
            else:
                print('Try again!')
        for key1 in keys:
             for val in values:
                 result[key1] = val
                 values.remove(val)
                 break
        
    return result
 
 