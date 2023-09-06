def prod(start, stop):
    """Defining prod() function with two variables 
    'start', 'stop' as input which are integers."""
    if start > stop:
        return None
    if start <= stop:
        result = 1
        for i in range(start, stop + 1):
            """Using for loop, we count the multiplication 
            of all integers in the given range (start, stop)"""
            result *= i
    return result


def word_count(st):
    """Defining word_count() function with 
    one variable 'st' as input which is a text file."""
    count = 0
    for word in st.split():
        """Using for loop, we count the number of words in a string, 
        additionally using thesplit() method."""
        count += 1
    return count
    """Return the number of words as a result."""
    

#beatles = open('/Users/wondamonsta/Downloads/Project for Mid-March_ Practice writing functions/Beatles.txt', 'r').read()
#snipping2 = open('/Users/wondamonsta/Downloads/Project for Mid-March_ Practice writing functions/Snipping2.txt', 'r').read()
#snipping3 = open('/Users/wondamonsta/Downloads/Project for Mid-March_ Practice writing functions-2/Snipping3.txt', 'r').read()

def wc(filename):
    """Defining wc() function with one variable 'filename' 
    as input which is a text file."""
    fileref = open(filename)
    """Opening our input file using function open()."""
    lines = fileref.readlines()
    """Reading all lines at once using readlines() method."""
    count_lines = 0
    characters = 0
    new_lines = str(lines).split(' ', -1)
    words = len(new_lines)
    for line in lines:
        """Using for loop, first we count the number of lines in a text file,
        then we count the number of characters in those lines."""
        count_lines += 1
        characters += len(line)
    #for word in str(lines).split():
        #"""Using for loop,  we conver the lines into a
        #string using str() method,
        #then we split the string into words,
        #and count them."""
        #words+=1
    print(count_lines,"\t",words,"\t",characters)
    """Print the number of lines, characters, and words as a result."""
