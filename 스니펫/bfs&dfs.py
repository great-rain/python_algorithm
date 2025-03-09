graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# def matrix_to_adj_list(matrix):
#     adj_list = {}
#     for i, row in enumerate(matrix):
#         # 각 노드에 대해 연결된 노드의 리스트를 생성합니다.
#         # 연결된 노드의 인덱스를 문자열로 변환하여 저장합니다.
#         adj_list[str(i)] = [str(j) for j, connected in enumerate(row) if connected == 1]
#     return adj_list
#
# # 인접 행렬
# matrix = [
#     [1, 1, 0],
#     [1, 1, 0],
#     [0, 0, 1]
# ]

# 인접 리스트로 변환
adj_list = matrix_to_adj_list(matrix)
print(adj_list)



def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            # graph[node]에 연결된 노드들을 스택에 추가
            # 스택이므로 나중에 추가된 노드부터 탐색
            stack.extend(reversed(graph[node]))
    return visited

# 'A'에서 시작하는 DFS 실행
print(dfs(graph, 'A'))



from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            # graph[node]에 연결된 노드들을 큐에 추가
            # 큐이므로 먼저 추가된 노드부터 탐색
            queue.extend(graph[node])
    return visited

# 'A'에서 시작하는 BFS 실행
print(bfs(graph, 'A'))