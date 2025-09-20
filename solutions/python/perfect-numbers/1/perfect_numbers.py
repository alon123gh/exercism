import math

def get_divisors(num: int):
    if num == 1: return []
        
    divisors = {1}
    for n in  range(2, math.isqrt(num)+1):
        if (num % n) == 0:
            divisors.add(n)
            divisors.add(num // n)
    return list(divisors)
    
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    classfication = None
    divisors = get_divisors(number)
    divisors_sum = sum(divisors)
    if divisors_sum == number:
        classfication = "perfect"
    if divisors_sum > number:
        classfication = "abundant"
    if  divisors_sum < number:
        classfication = "deficient"
    return classfication     
