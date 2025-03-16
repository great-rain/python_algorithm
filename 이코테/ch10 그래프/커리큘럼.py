"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""
import copy
from collections import deque

N = int(input())

indegree = [0] * (N+1)

graph = [[] for i in range(N+1)]
time = [0] * (N+1)


for i in range(1, N+1):
    input_list = list(map(int, input().split()))
    time[i] = input_list[0]
    for x in input_list[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topological_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for i in range(1, N+1):
        print(result[i])

topological_sort()