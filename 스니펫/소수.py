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

# 범위 구하기
prime = []
numbers = [1, 1] + [0] * 999999

for i in range(2, 1000001):
    if numbers[i] == 0:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            numbers[j] = 1

N, M = map(int, input().split())
for p in prime:
    if N <= p <= M:
        print(p)
    elif p > M:
        break
