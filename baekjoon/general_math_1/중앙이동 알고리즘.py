s = 2
for n in range(int(input())):
    s = s + 2 ** n

print(s**2)
"""
2 ^ 2
3 ^ 2  -- + 1
5 ^ 2  -- + 2
9 ^ 2  -- + 4
17 ^ 2  -- + 8

2의 제곱근으로 커짐 
"""