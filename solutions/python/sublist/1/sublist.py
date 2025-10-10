"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def is_equale(list_one, list_two):
    if len(list_one) != len(list_two):
        return False
    return all(ch1 == ch2 for ch1, ch2 in zip(list_one, list_two))    

def contains(list_a, list_b):
    if not list_a:
        return True #empty list
    if len(list_a) > len(list_b):
        return False
    for index in range(0,len(list_b) - len(list_a)+1):
        if list_a == list_b[index: index + len(list_a)]:
            return True
    return False        



def sublist(list_one, list_two):
    if is_equale(list_one, list_two):
        return EQUAL;
    if  contains(list_one, list_two):
        return SUBLIST
    if contains (list_two, list_one):   
        return SUPERLIST
    return UNEQUAL    