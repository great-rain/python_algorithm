# H, W = map(int, input().split())
#
# # board 만들기
# board = [input() for _ in range(H)]
#
# # 타일나눠기
# lowest_change = 64 # 다 바꾸는 경우
# for i in range(H-7):
#     for j in range(W-7):
#         # 시작이 W 인경우
#         change_board = 0
#         start_tile = 'W'
#         for r in range(i, i+8, 2):
#             for c in range(j, j+8, 2): # row 별로 체크하기 n + 2
#                 # 시작 칸 비교
#                 if start_tile != board[r][c]:
#                     change_board += 1
#
#                 # 옆칸이랑 비교
#                 if start_tile == board[r][c+1]:
#                     change_board += 1
#
#                 # 아래칸이랑 비교
#                 if start_tile == board[r+1][c]:
#                     change_board += 1
#
#                 # 대각선이랑 비교
#                 if start_tile != board[r+1][c+1]:
#                     change_board += 1
#
#         lowest_change = min(lowest_change, change_board)
#
#         # 시작이 B 인경우
#         change_board = 0
#         start_tile = 'B'
#         for r in range(i, i+8, 2):
#             for c in range(j, j+8, 2):
#                 # 시작 칸 비교
#                 if start_tile != board[r][c]:
#                     change_board += 1
#
#                 # 옆칸이랑 비교
#                 if start_tile == board[r][c+1]:
#                     change_board += 1
#
#                 # 아래칸이랑 비교
#                 if start_tile == board[r+1][c]:
#                     change_board += 1
#
#                 # 대각선이랑 비교
#                 if start_tile != board[r+1][c+1]:
#                     change_board += 1
#
#         lowest_change = min(lowest_change, change_board)
#
# print(lowest_change)

"""
최적화
"""
H, W = map(int, input().split())

# board 만들기
board = [input() for _ in range(H)]

def calculate_changes(board, start_tile, i, j):
    changes = 0
    for r in range(8):
        for c in range(8):
            # 현재 칸에서의 올바른 타일 색상 계산
            expected_tile = start_tile if (r + c) % 2 == 0 else ('B' if start_tile == 'W' else 'W')
            if board[i + r][j + c] != expected_tile:
                changes += 1
    return changes

lowest_change = 64  # 최대 가능한 변화 횟수

for i in range(H - 7):
    for j in range(W - 7):
        # 두 가지 시작 타일로 각각 계산
        changes_with_w = calculate_changes(board, 'W', i, j)
        changes_with_b = calculate_changes(board, 'B', i, j)

        # 더 적은 변화 횟수를 선택
        lowest_change = min(lowest_change, changes_with_w, changes_with_b)

print(lowest_change)