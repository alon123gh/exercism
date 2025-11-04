def primes(limit):
    if limit < 2:
        return []

    numbers = [True] * (limit+1)
    numbers[0:2] = [False] * 2
    for n in  range (2,limit+1):
        if numbers[n]:
            numbers[n+n:limit+1:n] = [False] * len(range(n+n, limit+1, n))
    return [index for index, is_prime in enumerate(numbers) if is_prime] 
