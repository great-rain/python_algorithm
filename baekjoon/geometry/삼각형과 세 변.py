while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if max(a, b, c)*2 - (a+b+c) >= 0:
        print("Invalid")
    else:
        if a == b == c:
            print('Equilateral')
        elif a == b or a == c or b == c:
            print('Isosceles')
        else:
            print('Scalene')