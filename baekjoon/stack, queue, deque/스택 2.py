import sys
stack = []
for _ in range(int(sys.stdin.readline().strip())):
    command = sys.stdin.readline().strip()
    if command[0] == '1':
        number = int(command.split()[1])
        stack.append(number)
    elif command == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == '3':
        print(len(stack))
    elif command == '4':
        print(1 if not stack else 0)
    elif command == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)
