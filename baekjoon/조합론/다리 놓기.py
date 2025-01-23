def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

for _ in range(int(input())):
    N, M = map(int, input().split())
    print(factorial(M)//(factorial(N)*factorial(M-N)))