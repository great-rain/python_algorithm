from math import ceil

n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
res = sum([ceil(i / t) for i in size])

print(res)
print(n // p, n % p)