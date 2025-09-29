import re
def is_isogram(string):
    clean_string =  re.sub("[^a-zA-Z]","",string).lower()
    return len(clean_string) == len(set(list(clean_string)))
