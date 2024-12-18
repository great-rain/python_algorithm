import sys
gat=['a','e','i','o','u', 'A','E','I','O','U']

while True:
    count = 0
    S = sys.stdin.readline()
    if S == '#\n':
        break
    for w in S:
        if w in gat:
            count += 1
    print(count)