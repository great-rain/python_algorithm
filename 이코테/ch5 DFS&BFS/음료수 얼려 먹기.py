"""
test case
# 3
4 5
00110
00011
11111
00000

# 8
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

추가테스트 케이스
# 5
5 5
01010
01010
01010
01010
01010

# 1
4 6
000000
011110
011110
000000

# 4
6 7
0010000
0111011
0000000
1101110
1100000
0001111

# 5
5 5
10001
00000
00100
00000
10001

# 1
3 3
000
000
000

# 0
3 3
111
111
111

# 1
1 1
1
"""

H, W = map(int, input().split())

shape = []
for i in range(H):
    shape.append([int(i) for i in input()])

visited = [[False] * W for _ in range(H)]
count = 0


# 오답
# def dfs(_shape: list, start_x: int, start_y: int):
#     for move_y in range(start_y, H):
#         for move_x in range(start_x, W):
#             if not visited[move_y][move_x]:
#                 if _shape[move_y][move_x] == 1:
#                     visited[move_y][move_x] = True
#                     return dfs(_shape, start_x, start_y)
#                 else:
#                     visited[move_y][move_x] = True
#                     return dfs(_shape, move_x, move_y)

def dfs(x, y):
    if x < 0 or x >= W or y < 0 or y >= H or visited[y][x] or shape[y][x] == 1:
        return

    visited[y][x] = True  # 방문 처리

    # 상, 하, 좌, 우 탐색
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)


for now_y in range(H):
    for now_x in range(W):
        if not visited[now_y][now_x]:
            visited[now_y][now_x] = True
            if shape[now_y][now_x] == 0:
                dfs(now_x, now_y)
                count += 1
print(count)

"""
풀다 막힌부분 1
0 인걸 체크하고 넘어갔는데 돌아오는 방법.
1이면 끊어주고 다시 "처음"으로 돌아와야함. 그러면 종료시점은?
--> 더이상 조회할게 없으면 종료

막힌부분 2
그러면 count 가 늘어나는 시점은? -> dfs 종료시점
--> 해결 방법 전체조회해서 얼음일때만 dfs 동작

틀린부분 1
for 문을 사용하게 되어 4방향이 아닌 오른쪽 아래로만 진행하게됨 
-> 왼쪽 아래로 진행하는 경우 파악이 안되어서 오답 발생

개선부분 1
4중 for문 이상이라 성능 문제 심각
전체를 조회하면서 단순 조회로 방문 파악하는게 속도 개선에 더 도움이 됨

수정 코드
def count_ice_creams(n, m, ice_tray):
    # 방문 여부 체크를 위한 2차원 리스트
    visited = [[False] * m for _ in range(n)]
    
    # DFS 탐색 함수 정의
    def dfs(x, y):
        # 범위를 벗어나면 즉시 종료
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        
        # 방문하지 않았고, 구멍(0)인 경우 탐색 진행
        if not visited[x][y] and ice_tray[x][y] == 0:
            visited[x][y] = True  # 방문 처리
            
            # 상, 하, 좌, 우 탐색
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            
            return True
        return False
    
    # 아이스크림 개수 세기
    ice_cream_count = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j):  # 새로운 덩어리를 찾았을 때
                ice_cream_count += 1

    return ice_cream_count

# 입력 예제
n, m = 4, 5
ice_tray = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

# 결과 출력
print(count_ice_creams(n, m, ice_tray))  # 출력: 3
"""
