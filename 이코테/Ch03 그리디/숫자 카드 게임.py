N, M = map(int, input().split())
res = 0

for i in range(N):
    arr = list(map(int, input().split()))
    m = 10001
    for a in arr:
        m = min(m, a)
    res = max(res, m)

print(res)