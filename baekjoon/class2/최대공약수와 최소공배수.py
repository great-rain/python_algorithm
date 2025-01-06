a, b = map(int,input().split())
m = a * b
while b:
    a, b = b, a % b

gcd = a
print(gcd)
print(m//gcd)