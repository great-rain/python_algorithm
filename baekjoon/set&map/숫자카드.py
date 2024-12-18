import sys
N1 = int(sys.stdin.readline())
card_set = {val: 1 for idx, val in enumerate([i for i in map(int, sys.stdin.readline().split())])}
N2 = int(sys.stdin.readline())
my_set = [i for i in map(int, sys.stdin.readline().split())]
result = []
for i in my_set:
    result.append(card_set.get(i, 0))

print(*result)