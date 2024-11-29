N, M = map(int, input().split())


matrix = [[], []]
for m in range(2):
    for i in range(N):
        matrix[m].append([int(i) for i in input().split()])


for n in range(N):
    line = []
    for m in range(M):
        line.append(matrix[0][n][m] + matrix[1][n][m])

    print(' '.join(map(str, line)))


"""
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
B = [list(map(int, input().split())) for i in range(N)]
for i in range(N):
    for j in range(M):
        A[i][j] = A[i][j] + B[i][j]
    print(*A[i])
"""