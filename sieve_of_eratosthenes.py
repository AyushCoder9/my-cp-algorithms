def sieve_of_eratosthenes(n):
    prime = [True for i in range(n + 1)]
    prime[0] = prime[1] = False
    p = 2

    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    prime_numbers = []
    for p in range(2, n + 1):
        if prime[p]:
            prime_numbers.append(p)
            
    return prime_numbers

limit = 30
primes_list = sieve_of_eratosthenes(limit)
print(f"Following are the prime numbers smaller than or equal to {limit}:")
print(primes_list)
