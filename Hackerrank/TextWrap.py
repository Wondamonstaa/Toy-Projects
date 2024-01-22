import textwrap

def wrap(string, max_width):
    
    wrapped = textwrap.wrap(string, max_width)
    
    result = ""
    
    for char in wrapped:
        result += char + "\n"

    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
