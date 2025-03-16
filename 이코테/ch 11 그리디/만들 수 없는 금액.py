"""
5
3 2 1 1 9

5
1 2 3 4 5
"""
N = int(input())
coins = sorted((map(int, input().split())))

target = 1

for x in coins:
    if target < x:
        break
    target += x

print(target)
