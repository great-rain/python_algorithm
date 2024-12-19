import sys

N = int(sys.stdin.readline().strip())
NL = list(map(int, sys.stdin.readline().strip().split()))

M = int(sys.stdin.readline().strip())
ML = list(map(int, sys.stdin.readline().strip().split()))

count = {}
for i in NL:
    if count.get(i, 0):
        count[i] += 1
    else:
        count[i] = 1
ans = []
for m in ML:
    ans.append(count.get(m, 0))

print(*ans)