import math

def is_prime(number):
    if number == 1:
        return False
    for factor  in range (2, int(math.sqrt(number))+1):
        if number % factor == 0:
            return False
    return True
    
def validate(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    if number < 0:    
        raise ValueError('Only posivite numbers supported')

def primes_gen():
    number = 1
    while True:
        if is_prime(number):
            yield number
        number+=1
        
def prime(number):
    validate(number)
    primes = primes_gen()
    for index, prime  in enumerate(primes):
         if index == number -1:
             break
       
    return prime          
  