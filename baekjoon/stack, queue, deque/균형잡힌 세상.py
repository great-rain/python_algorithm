import sys
while True:
    text = sys.stdin.readline().strip('\n')
    if text == '.':
        break
    stack = []

    condition = True
    for s in text:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    condition = False
                    break
            else:
                condition = False
                break
        if s == '[':
            stack.append(s)
        elif s == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    condition = False
                    break
            else:
                condition = False
                break

    if not condition or stack:
        print('no')
    else:
        print('yes')