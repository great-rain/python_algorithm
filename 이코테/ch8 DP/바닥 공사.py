"""
# 바텀 업 방식 -> n번째 에서 늘어난 길이 만큼 추가 더 해주면 되니까
1 칸 늘어날 경우 -> 1가지 경우밖에없음
2 칸 늘어날 경우 -> 2가지 경우의수

a(n) = a(n-1) + a(n-2) * 2
"""
# 바텀 업 방식 -> n번째 에서 늘어난 길이 만큼 추가 더 해주면 되니까
N = int(input())
matrix = [0] * 1001

matrix[0] = 1
matrix[1] = 3

for i in range(3, N+1):
    matrix[i] = (matrix[i-1] + matrix[i-2] * 2) % 796796

print(matrix[N])
