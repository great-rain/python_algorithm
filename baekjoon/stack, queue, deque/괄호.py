for _ in range(int(input())):
    stack = []
    for i in input():
        if i == '(':
            stack.append(True)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(False)
                break
    if stack:
        print('NO')
    else:
        print('YES')