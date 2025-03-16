"""
5
2 3 1 2 2
"""
N = int(input())
travelrs = sorted(map(int, input().split()))
result = 0
count = 0
for fear in travelrs:
    count += 1
    if count >= fear:
        result += 1
        count = 0

print(count)