xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())
# brute force
answer = []
for x in range(1, 1001):
    for y in range(1, 1000):
        if abs(x-xc) == abs(xa-xb) and abs(y-yc) == abs(ya-yb):
            if (x == xa or x == xb or x == xc) and (y == ya or y == yb or y == yc):
                answer = [x, y]

print(*answer)


"""
x = [0,0,0]
y = [0,0,0]
for i in range(3):
    x[i], y[i] = map(int,input().split())
x.sort()
y.sort()
if x[0]==x[1]:
    a = x[2]
else:
    a = x[0]
if y[0]==y[1]:
    b = y[2]
else:
    b = y[0]

print(a,b)
"""

