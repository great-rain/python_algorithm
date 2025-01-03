for _ in range(int(input())):
    flag = 1
    count = 0
    for i in input():
        if i == 'O':
            count = count + flag
            flag += 1
        else:
            flag = 1
    print(count)