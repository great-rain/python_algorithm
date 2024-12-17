import sys
I = sys.stdin.readline
N = int(I())
a = []
for i in range(N):
    a.append([int(i) for i in I().split()])
a.sort(key= lambda x:(x[1], x[0]))
for i in a:
    print(*i)
