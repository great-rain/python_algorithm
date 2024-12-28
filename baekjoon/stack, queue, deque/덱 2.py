import sys
from collections import deque
Input = sys.stdin.readline
dq = deque()

for _ in range(int(Input())):
    n = Input().strip()
    if n[0] == '1':
        dq.appendleft(n[2:])
    elif n[0] == '2':
        dq.append(n[2:])
    elif n[0] == '3':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif n[0] == '4':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif n[0] == '5':
        print(len(dq))
    elif n[0] == '6':
        print(1 if not dq else 0)
    elif n[0] == '7':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif n[0] == '8':
        if dq:
            print(dq[-1])
        else:
            print(-1)