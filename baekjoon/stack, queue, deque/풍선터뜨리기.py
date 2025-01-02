import sys
from collections import deque
N = int(sys.stdin.readline().strip())
deq = deque(enumerate(map(int, sys.stdin.readline().strip().split())))
res = []
while deq:
    idx, now_turn = deq.popleft()
    res.append(idx + 1)

    if now_turn > 0:
        deq.rotate(-(now_turn - 1))

    elif now_turn < 0:
        deq.rotate(-now_turn)

print(' '.join(map(str, res)))