import sys
from collections import deque

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
C = list(map(int, sys.stdin.readline().strip().split()))

queue = deque([])
for i in range(N):
    if A[i] == 0:
        queue.append(B[i])

for i in range(M):
    queue.appendleft(C[i])
    print(queue.pop(), end=' ')
