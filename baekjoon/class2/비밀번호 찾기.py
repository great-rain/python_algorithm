import sys
Input = sys.stdin.readline
write = sys.stdout.write
N,M = map(int,Input().split())
pd = {}
for _ in range(N):
    site, pw = Input().split()
    pd[site] = pw
for _ in range(M):
    write(pd[input()]+'\n')