def build(s):
    """The build(s) function takes one string 's' as input and returns a dictionary."""
    chain = dict()
    #test_chain = dict()
    tokens = s.split()
    if type(s) == str:
        for token in tokens:
            tokens_updated = token.split(',')
            #print(tokens_updated)
            key = tokens_updated[0]
            value = tokens_updated[1]
            chain[key] = value
        else:
            pass
    return chain


def lookup(dict_list, key_name):
    """After taking 2 inputs (dict_list is a dictionary with the contact list,
    string_name is a string containing a name), the function lookup() 
    outputs the value associated with the key or name in the dictionary."""
    if key_name in dict_list:
        result = dict_list[key_name]
    return result


def combo(word_pairs, name):
    """combo() function takes two string inputs
    (word_pairs consisting of a str(name) and a str(phone number), 
     separated by ',', and a name. Combo() outputs the phone number (value)
     associated with the name (key)."""
    for item in word_pairs:
        if word_pairs.count(item) > 0:
            new_dict = build(word_pairs)
        else:
            pass
    target_new = lookup(new_dict, name)
    return target_new
