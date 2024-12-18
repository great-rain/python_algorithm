import sys
status = {}
for _ in range(int(sys.stdin.readline())):
    n, s = map(str, sys.stdin.readline().split())
    if s == 'enter':
        status[n] = 1
    else:
        status[n] = 0

a = [k for k, v in status.items() if v == 1]
for i in sorted(a, reverse=True):
    print(i)