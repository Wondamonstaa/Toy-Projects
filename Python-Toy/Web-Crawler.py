import urllib.request as ur
import re


def get_url(s):
   """Defining the function get_url(s)."""
   answer = ''
   if '<a href=' in s:
      """Using for loop to find a part of the string we are looking for."""
      start = s.find('a href=') + 8
      s2 = s[start: -1]
      for i in s2:
          if i not in '"':
              answer += i
          else:
              break
   else:
      answer = -1
   return answer    
"""Returning the function's result back to the caller."""

def list_all_links(s):
    """Defining the function list_all_links(s) which gets a string as input."""
    list_links = list()
    for link in s:
        link = get_url(s)
        if link ==-1:
            break
        else:
            pass
        list_links +=[link]
        
        s = s[s.find('<a href=') + 9:]
        """'9' is the length of <a href=, so we find the location of it, 
        we know the string we want starts right after it."""
        end_pos = s.find('"')
        s = s[end_pos:]
    return list_links
"""Returning the function's result back to the caller."""

def get_addresses(content):
     '''Input can be either str type or bytes type from a urllib read. 
     Credit: Professor Sloan and the TA's.'''
     #re package wants str type, not bytes
     strings = re.findall('[a-zA-Z0-9_.]*[@][a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
                             str(content))
     #Some addresses have a trailing period. Need to get rid of it...
     for x in range(0, len(strings)):
         if strings[x].endswith("."):
             strings[x] = strings[x][0:len(strings[x])-1]
     return list(dict.fromkeys(strings))     # remove duplicates



def crawl(start, limit):
    """Defining the function called crawl(start, limit)
    which returns a list of all the unique email 
    addresses reachable from the webpage whose URL is 'start', 
    and the function stops when reaches the 'limit' web pages."""
    target = [start]
    visited = list()
    final_list = list()
    count = 0
    
    while len(target) < limit:
        if count >= len(target):
            break
        address = target.pop()
        for link1 in list_all_links(str()):
            if link1 not in target:
                target.append(link1)
            else:
                pass
        if address not in visited:
            content = ur.urlopen(address).read()
            list_links = list_all_links(str(content))
            final_list += get_addresses(content)
            for i in list_links:
                target.append(i)
            visited.append(address)
            for link in list_all_links(str(content)):
                target.append(link)
                
        if len(visited) >= limit:
            break
    return sorted(list(set(final_list)))
    """Returning the function's result back to the caller.
    Here I used sorted function to organize the list's 
    elements in alphabetical order, at the same time removing 
    duplicates using set()."""
            

