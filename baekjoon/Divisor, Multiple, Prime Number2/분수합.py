def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
x0, x1 = map(int, input().split())
y0, y1 = map(int, input().split())
p = x1*y1
c = x0*y1 + y0*x1
g = gcd(p, c)
print(c//g, p//g)

