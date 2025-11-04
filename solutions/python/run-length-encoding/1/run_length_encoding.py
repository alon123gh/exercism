from itertools import groupby
import re

def decode(string):
    if not string:
        return ""

    count = None
    key_pos = None
    result = ""
    while string:
        match = re.match(r"^(\d+)", string)
        if not match:
            count = 1
            key_pos = 0
        else:
            count = int(match.group(0))
            key_pos = match.end()
            
        key = string[key_pos]
        result +=  key*count
        string = string[key_pos+1:]
    return result            
    


def encode(string):
     if not string:
         return ""
     result = ""    
     for key, group in groupby(string):
         count  = len(list(group))
         if count > 1:
             result += str(count)
         result += key
     return result    
