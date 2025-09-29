import itertools

def is_trinagle(sides):
    if  any(side == 0 for side in sides):
        return False

    #triangle inequlity 
    side_pairs = itertools.combinations(sides, 2)
    for side_pair  in side_pairs:
        if sum(list(side_pair)) < sum(set(sides)-set(side_pair)):
            return False
            
    return True        
    
        
def equilateral(sides):
      return is_trinagle(sides) and len(set(sides)) == 1


def isosceles(sides):

    if equilateral(sides):
        return True
    return  is_trinagle(sides) and len(set(sides))==2


def scalene(sides):
   return  is_trinagle(sides) and len(set(sides))==3