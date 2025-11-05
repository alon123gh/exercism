from math import isqrt, gcd

def validate_pair(m,n):
   return (m - n) % 2 != 0 and gcd(m, n) == 1
    
def triplets_with_sum(number):
    result = []
    for m in range(2, isqrt(number // 2) + 1):
        for n in range(1, m):
            if not validate_pair(m,n):
                 continue
            if number % (2 * m * (m + n)) == 0:
                k = number // (2 * m * (m + n))
                result.append(sorted([
                    k * (m**2 - n**2),
                    k * (2 * m * n),
                    k * (m**2 + n**2)
                ]))
    return result