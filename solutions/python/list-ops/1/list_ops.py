def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []
    for lst in lists:
        result += lst
    return result    
        


def filter(function, list):
    return [element for element in list if function(element)]


def length(list):
    if not list :
        return 0
    return list.index(list[-1])+1


def map(function, list):
    return [function(element) for element in list]


def foldl(function, list, initial):
    accu = initial
    for element in list:
        accu = function(accu, element) 
    return accu

def foldr(function, list, initial):
    accu = initial
    for element in reversed(list):
        accu = function(accu, element)
    return accu

def reverse(list):
    return list[-1::-1]
