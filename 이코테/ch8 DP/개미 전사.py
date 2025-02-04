"""
# 8
4
1 3 1 5

# 9
5
1 2 3 4 5

# 10
5
1 6 2 4 3
"""


N = int(input())
foods = list(map(int, input().split()))
matrix = [0] * N

# 바텀업

matrix[0] = foods[0]
matrix[1] = foods[1]

for i in range(2, N):
    matrix[i] = max(matrix[i - 1], matrix[i - 2] + foods[i])

print(matrix[-1])