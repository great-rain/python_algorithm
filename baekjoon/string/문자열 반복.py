for _ in range(int(input())):
    n, s = map(str, input().split())
    print(''.join([i*int(n) for i in s]))