"""
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4

"""
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


# 두 원소가 속한 집합을 찾기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())

parent = [0] * (v + 1)
for i in range(1, v+1):
    parent[i] = i

edges = []

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

# 비용순으로 정리
edges.sort()
result = 0
last = 0

for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c # 전부 연결
        last = c # 가장 큰 마지막꺼 새로 갱신

print(result - last) # 최소로 연결을 전부 해버린 다음에 가장큰걸 빼버림 -> 최소 연결 방법
