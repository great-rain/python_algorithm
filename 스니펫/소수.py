# 하나 확인 방법
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 에라토스테네스의 체
def sieve_of_eratosthenes(limit):
    prime = [True for _ in range(limit+1)]
    p = 2
    while (p * p <= limit):
        if (prime[p] == True):
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, limit) if prime[p]]
    return prime_numbers
