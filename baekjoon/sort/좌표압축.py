import sys
N = int(sys.stdin.readline())
co = [i for i in map(int, sys.stdin.readline().split())]
order = {val: idx for idx, val in enumerate(sorted(set(co)))}
result = ' '.join(str(order[i]) for i in co)
sys.stdout.write(result)