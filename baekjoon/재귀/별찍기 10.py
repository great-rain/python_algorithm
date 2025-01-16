n = 27
arr = [['*' for i in range(n)] for j in range(n)]


def del_star(x, y, size):
    # 종료 조건: 사이즈가 1이면 더 이상 작업하지 않음
    if size == 1:
        return

    # 비울 부분의 시작과 끝 계산 & 비우기
    start = size // 3
    for i in range(start):
        for j in range(start):
            arr[x + start + i][y + start + j] = ' '

    # 나머지 8개의 작은 부분에 대해 재귀 호출
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:  # 가운데 부분은 이미 비움
                continue
            del_star(x + i * start, y + j * start, start)
# 재귀 호출 시작
del_star(0, 0, n)

# 결과 출력
for row in arr:
    print(''.join(row))
# def del_star(arr: list) -> list:
#     start = len(arr) // 3
#     end = len(arr) // 3 * 2 - 1
#     if start == end:
#         return
#
#     for i in range(start, end + 2):
#         for j in range(start, end + 2):
#             arr[i][j] = ' '
#
#     for p in range(start, len(arr), start):
#         return del_star(arr[:p][:p])


# res = del_star(arr)
# for i in res:
#     print(''.join(i))

# for _ in range(len(arr)):
#     print(''.join(del_star(arr)))

# 1번 풀이
import sys
sys.setrecursionlimit(10 ** 6)
def paint_star(LEN):
    DIV3 = LEN // 3
    if LEN == 3:
        g[1] = ['*', ' ', '*']
        g[0][:3] = g[2][:3] = ['*'] * 3
        return

    paint_star(DIV3)

    for i in range(0, LEN, DIV3):
        for j in range(0, LEN, DIV3):
            if i != DIV3 or j != DIV3:
                for k in range(DIV3):
                    g[i + k][j:j + DIV3] = g[k][:DIV3]


n = int(sys.stdin.readline().strip())
g = [[' ' for _ in range(n)] for _ in range(n)]

paint_star(n)

for i in range(n):
    for j in range(n):
        print(g[i][j], end='')
    print()

# 2번 풀이
import sys
sys.setrecursionlimit(10 ** 6)
def append_star(LEN):
    if LEN == 1:
        return ['*']

    Stars = append_star(LEN // 3)
    L = []

    for S in Stars:
        L.append(S * 3)
    for S in Stars:
        L.append(S + ' ' * (LEN // 3) + S)
    for S in Stars:
        L.append(S * 3)
    return L


n = int(sys.stdin.readline().strip())
print('\n'.join(append_star(n)))