import sys
l = numbers = [int(line.strip()) for line in sys.stdin]
m = max(l)
print(m)
print(l.index(m)+1)