import sys
while True:
    lines = sorted(map(int, sys.stdin.readline().split()))
    if lines[0] == 0:
        break
    if lines[0]**2 + lines[1]**2 == lines[2]**2:
        print('right')
    else:
        print('wrong')