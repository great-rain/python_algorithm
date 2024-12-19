import sys
N, M = map(int, sys.stdin.readline().strip().split())

D = {}
A = []
for _ in range(N):
    D[sys.stdin.readline().strip()] = True

for _ in range(M):
    S = sys.stdin.readline().strip()
    if D.get(S, False):
        A.append(S)
A.sort()
sys.stdout.write(str(len(A))+'\n')
sys.stdout.write("\n".join(A))