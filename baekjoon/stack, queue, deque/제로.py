import sys
Input = sys.stdin.readline
stack = []
for _ in range(int(Input())):
    n = int(Input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))