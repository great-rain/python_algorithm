'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''
N, M = map(int, input().split())
now_x, now_y, direction = map(int, input().split())

maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

# 방문 체크 배열
checked = [[False for _ in range(M)] for _ in range(N)]
checked[now_x][now_y] = True  # 시작 위치 방문 처리
count = 1  # 방문도 1

# 방향 vector
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turning(direction: int) -> int:
    if direction == -1:
        return 3
    return direction - 1


def move_recursive(x, y, direction, count):
    for _ in range(4):
        # 왼쪽으로 회전
        direction = turning(direction)
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 이동 가능 여부 확인. 가능하면 이동
        if 0 <= nx < N and 0 <= ny < M and not checked[nx][ny] and maps[nx][ny] == 0:
            """
            0 <= nx < N and 0 <= ny < M 이동가능 범위
            checked[nx][ny] 미방문
            maps[nx][ny] 육지임
            """
            checked[nx][ny] = True  # 방문 처리
            return move_recursive(nx, ny, direction, count + 1)

    # 네 방향 모두 이동할 수 없는 경우
    # 뒤로 이동
    nx = x - dx[direction]
    ny = y - dy[direction]

    # 못가는 경우 종료
    if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 0:
        """
        0 <= nx < N and 0 <= ny < M 이동가능 범위
        maps[nx][ny] 육지 but 이미 방문한 구역. -> 그냥 방문함
        """
        return move_recursive(nx, ny, direction, count)
    else:
        """
        바다이거나 움직일수 없는 경우
        """
        # 뒤로 갈 수 없는 경우 종료
        return count


result = move_recursive(now_x, now_y, direction, count)
print(result)


# 후기
"""
헤맨 부분
1. 이동 가능 한 영역을 함수로 따로 빼서 연산하려 하니 코드가 이동코드와 꼬여버려서 코드가 난잡해졌다. 
    -> 정리해서 움직일수 있는 경우와 못움직은 경우로 나눠저 풀이

개선사항
1.
    checked = [[False for _ in range(M)] for _ in range(N)] 
    대신 checked = [[False]*M for _ in range(N)] 이 연산 더 빠름

2. 
    turning 대신 direction = (direction - 1) % 4 써도 됐음
"""