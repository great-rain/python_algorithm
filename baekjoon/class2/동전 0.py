import sys
N, K = map(int, sys.stdin.readline().split())
coins = []
count = 0
for _ in range(N):
    coins.append(int(sys.stdin.readline()))
coins.sort(reverse=True)
for c in coins:
    if K / c >= 1:
        res = K//c
        count += res
        K -= res*c
print(count)