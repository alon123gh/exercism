
def find_multiples (limit, multiplier):
   if multiplier == 0:
       return {}
   return set(range(multiplier,limit,multiplier))
    
def sum_of_multiples(limit, multiples):
    total_set = set()
    for multiplier in multiples:
        total_set.update(find_multiples(limit, multiplier))
    return sum(total_set)