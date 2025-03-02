"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

# 3

4 2
1 3
2 4
3 4

# -1
"""

INF = int(1e9) # 무한

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 거리는 모두 1로 설정
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

# # x 까지 최단거리
# for c in range(1, x + 1):
#     for a in range(1, x + 1):
#         for b in range(1, x + 1):
#             graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

# # x 에서 k 까지 최단거리
# for c in range(x, k):
#     for a in range(x, k):
#         for b in range(x, k):
#             graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for c in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

distance = graph[1][k] + graph[k][x] # k까지거리 + k부터 x까지 거리
for i in range(n+1):
    graph[i][i] = 0
    for j in range(n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        print(graph[i][j],end =" ")
    print()

if distance >= INF:
    print(-1)
else:
    print(distance)
