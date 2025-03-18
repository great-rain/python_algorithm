n = int(input())
score_board = []

for _ in range(n):
    data = list(map(str, input().split()))
    name = data[0]
    K, E, M = map(int, data[1:])
    score_board.append((name, K, E, M))

score_board.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in score_board:
    print(i[0])