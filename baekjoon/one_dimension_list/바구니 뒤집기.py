N, M = map(int, input().split())
l = [i for i in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    l[i-1:j] = l[i-1:j][::-1]

print(*l)