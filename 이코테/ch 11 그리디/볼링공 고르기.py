"""
5 3
1 3 2 3 2

# 8

8 5
1 5 4 3 2 4 5 2
# 25

5 2
2 2 2 2 2 
"""

N, M = map(int, input().split())
bowling_balls = list(map(int, input().split()))
count = 0
for i in range(N):
    for j in range(i+1, N):
        if bowling_balls[i] != bowling_balls[j]:
            count += 1

print(count)