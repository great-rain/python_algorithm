import sys
# print(sys.stdin.readlines())

result = ''
matrix = []
max_len = 0
for i in range(5):
    ls = [i for i in input()]
    max_len = max(max_len, len(ls))
    matrix.append(ls)

for j in range(max_len):
    for i in range(5):
        if len(matrix[i]) > j:
            result += matrix[i][j]

print(result)
"""
0, 0
1, 0
2, 0
3, 0
4, 0
0, 1
1, 1
2, 1
3, 1
4, 1
0, 2
1, 2
2, 2
3, 2
4, 2
0, 3
1, 3
2, 3
3, 3
4, 3
0, 4
1, 4
2, 4
3, 4
4, 4
0, 5
1, 5 -> X
2, 5
3, 5
4, 5

"""

"""
n = [input() for i in range(5)]

for i in range(15):
    for j in range(5):
        if i < len(n[j]):
            print(n[j][i],end='')

"""