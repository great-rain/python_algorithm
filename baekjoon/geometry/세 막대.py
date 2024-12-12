m = [i for i in map(int, input().split())]

if m[0] == m[1] == m[2]:
    print(m[0]+m[1]+m[2])
else:
    m = sorted(m)
    if m[2] >= m[0] + m[1]:
        print((m[0]+m[1])*2-1)
    else:
        print(m[0] + m[1] + m[2])
