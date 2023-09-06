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


def frequency_table(s):
    """This function takes as input a string and returns the word frequencies in it."""
    tokens = s.split()
    token_list = list(tokens)
    if type(s) == str:
        d = build_dictionary(token_list)
        #print(type(d))
        result = dict(sorted(d.items(), reverse=False))
        #print(type(result))
        #print(result)
        #keys_values = result.items()
        #new_d = {str(key): str(value) for key, value in keys_values}
        for key, value in result.items():
            result = print("{item1}: {item2}".format(item1 = key, item2 = value))

    else:
        print("Try again!")
    return result



#`Bob: 1`
#`bob: 2`
#`hey: 1`
#`hi: 2`


