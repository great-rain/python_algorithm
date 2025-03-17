"""
4 4 2 1
1 2
1 3
2 3
2 4

# 4
"""
from collections import deque

# bfs 로해서 k번 타고 들어갔을때 node의 갯수들 count

# 초기값 세팅
N, M, K, X = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}

# dfs 구현
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (N+1)
distance[X] = 0

q = deque([X])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in distance:
    if i == K:
        check=True
        print(i)

if not check:
    print(-1)