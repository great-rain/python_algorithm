import sys
N = int(sys.stdin.readline().strip())
students = list(map(int, sys.stdin.readline().split()))

stack = []

now_turn = 1
for s in students:
    stack.append(s)

    while stack and stack[-1] == now_turn:
        stack.pop()
        now_turn += 1

print('Sad') if stack else print('Nice')