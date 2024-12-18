import sys
N, M = map(int, sys.stdin.readline().split())
s = set()
for _ in range(N):
    s.add(sys.stdin.readline().strip())

count = 0
for _ in range(M):
    a = sys.stdin.readline().strip()
    if a in s:
        count += 1

print(count)