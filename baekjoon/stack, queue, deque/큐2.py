from collections import deque
import sys
dq = deque()

for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    if ' ' in s:
        command, number = s.split()
    else:
        command = s

    if command == 'push':
        dq.append(number)
    elif command == 'pop':
        if dq:
            print(dq[0])
            dq.popleft()
        else:
            print(-1)
    elif command == 'size':
        print(len(dq))
    elif command == 'empty':
        print(0) if dq else print(1)
    elif command == 'front':
        print(dq[0]) if dq else print(-1)
    elif command == 'back':
        print(dq[-1]) if dq else print(-1)