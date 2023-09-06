def build_dictionary(s):
    """The build(s) function takes one string 's' as input and returns a dictionary."""
    target = s
    final_dict = dict()
    if type(target) == list:
        for i in range(len(target)):
            key = target[i]
            counter = 0
            for j in range(i,len(target)):
                counter = target.count(key)
            count = dict({key:counter})
            if key not in final_dict.keys():
                final_dict.update(count)
            else:
                pass
    else:
        print("Please, enter a list.")
    return final_dict


#The next two functions must both call build_dictionary
#Write a function frequency_table() that takes as input a string, 
#and returns the word frequencies in that string, sorted by words. 
#Specifically, it returns a string that contains newlines with one line per word:
    
#2. Initialize a new empty list. +
#3. Now append the word to the new list from previous string if that word is not present in the new list.
#4. Iterate over the new list and use count function (i.e. string.count(newstring[iteration])) to find the frequency of word at each iteration.
    
def frequency_table(s):
    """This function takes as input a string and returns the word frequencies in it."""
    tokens = s.split()
    nameset=set(tokens)
    if type(s) == str:
        d={name:tokens.count(name) for name in nameset}
        result = sorted(d.items(), key=lambda x: x[1], reverse=False) 
        #ex_list = list(result)
        #final_result = ex_list.sort()
        dict_items = sorted(result)
        
    else:
        print("Try again!")
    return dict(dict_items)

#for key, value in student_score.items():
    #print(key, ' : ', value)