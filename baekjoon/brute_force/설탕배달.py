N = int(input())

count = 2000
for f in range(1001):
    for t in range(1001):
        if 5 * f + 3 * t == N:
            count = min(count, f+t)

print(-1) if count == 2000 else print(count)


"""
# 소거법 풀이
x = int(input())
a = 0
while x >= 0:
    if x % 5 == 0:
        a += (x//5)
        print(a)
        break
    x = x - 3
    a = a + 1
else:
    print(-1)
"""

