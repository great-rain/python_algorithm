"""
https://www.acmicpc.net/problem/1260
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
"""
from collections import deque

N, M, V = map(int, input().split())

# 인접 리스트 사용
graph = {i: [] for i in range(1, N+1)} # 조회속도 개선을 위한 dictionary 사용

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 리스트 초기화
dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)

# DFS 함수 (재귀)
def dfs(node_idx):
    dfs_visited[node_idx] = True
    print(node_idx, end=' ')
    for next_node in sorted(graph[node_idx]):  # 작은 번호부터 방문 (같은 위치의 노드 인 경우)
        if not dfs_visited[next_node]:
            dfs(next_node)

# BFS 함수 (큐)
def bfs(start_node):
    q = deque([start_node])
    bfs_visited[start_node] = True

    while q:
        node = q.popleft()
        print(node, end=' ')
        for next_node in sorted(graph[node]):  # 작은 번호부터 방문 (같은 위치의 노드 인 경우)
            if not bfs_visited[next_node]:
                q.append(next_node)
                bfs_visited[next_node] = True

dfs(V)
print()
bfs(V)