"""
# 10
5 6
101010
111111
000001
111111
111111

# 7
4 4
1111
1001
1011
1111

# -1 못가는 경우
4 4
1111
1001
1110
0001

# 15
5 5
11110
00010
11110
10000
11111

# 5
5 1
1
1
1
1
1

# 5
1 5
11111

"""
H, W = map(int, input().split())

maps = [[int(w) for w in input()] for _ in range(H)]
vector = [(0, 1), (1, 0), (0, -1), (-1, 0)]

from collections import deque


def bfs(maps, x, y):
    queue = deque([(x, y)])

    while queue:
        dx, dy = queue.popleft()

        for v in vector: # 움직일수 있는 경우의 수를 생각하여 이동
            move_x, move_y = v[0] + dx, v[1] + dy

            # 목적지 도달하면 반환
            if move_x == H - 1 and move_y == W - 1:
                return maps[dx][dy] + 1  # 현재 값에서 +1

            # 움직일 수 있는 곳 찾기
            if 0 <= move_x < H and 0 <= move_y < W and maps[move_x][move_y] == 1:
                maps[move_x][move_y] = maps[dx][dy] + 1  # 방문 처리 (거리 누적)
                queue.append((move_x, move_y)) # 이동한 위치 큐에 저장

    return -1  # 도달 불가능할 경우


print(bfs(maps, 0, 0))