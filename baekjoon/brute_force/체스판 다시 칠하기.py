H, W = map(int, input().split())

# board 만들기
board = [[] for _ in range(H)]
for i in range(H):
    line = input()
    for j in range(W):
        board[i].append(line[j])

# 타일나눠기
lowest_change = 64
for i in range(H-7):
    for j in range(W-7):
        # row 별로 체크하기 n + 2
        change_board = 0
        for r in range(i, i+7):
            for c in range(j, j+7, 2):
                # 옆칸이랑 비교
                if board[r][c] == board[r][c+1]:
                    change_board += 1

        lowest_change = min(lowest_change, change_board)

print(lowest_change)