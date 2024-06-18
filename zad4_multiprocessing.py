def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end+1):
        if is_prime(num):
            primes.append(num)
    # return primes
    prime_pairs = []
    for prim_num in range(len(primes)-1):
        if primes[prim_num+1] - primes[prim_num] == 2:
            prime_pairs.append((primes[prim_num], primes[prim_num+1]))
    return prime_pairs


if __name__ == '__main__':
    result = find_primes(1, 1000)
    print(result)
    