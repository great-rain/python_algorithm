def gcd(a, b):
    while a % b != 0:
        tmp = a % b
        a = b
        b = tmp

    return b


for i in range(int(input())):
    M, N = map(int, input().split())
    print(M * N // gcd(M, N))
