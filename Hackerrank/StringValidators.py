if __name__ == '__main__':
    s = input()
    rules = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]
    for rule in rules:
        print(any(map(rule, s)))

    
