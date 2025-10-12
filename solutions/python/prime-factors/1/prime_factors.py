

import math

def is_prime(number):
    if number == 1:
        return False
    for factor  in range (2, int(math.sqrt(number))+1):
        if number % factor == 0:
            return False
    return True
    
def primes_gen():
    
    number = 2 
    while True:
        if is_prime(number):
            yield number
        number +=1 

    

def factors(value):
   factors = []
   if value == 1:
       return factors

   primes = primes_gen()      
   current_prime = next(primes) 
   while not is_prime(value):
      if value % current_prime == 0:
          factors.append(current_prime)
          value /= current_prime
      else:
        current_prime = next(primes)
   factors.append(value)       
   return factors        
    
    
