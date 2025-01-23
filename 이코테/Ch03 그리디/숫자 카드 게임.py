import sys
N, M = map(int, input().split())
matrix = [list(map(int, row.split())) for row in sys.stdin.read().strip().split('\n')]
print(matrix[N-1][M-1])