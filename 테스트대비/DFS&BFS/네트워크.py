def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1 #DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
    return answer

def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1: #연결된 컴퓨터
            if visited[connect] == False:
                DFS(n, computers, connect, visited)

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            BFS(n, computers, com, visited)
            answer += 1
    return answer

def BFS(n, computers, com, visited):
    visited[com] = True
    queue = []
    queue.append(com)
    while len(queue) != 0:
        com = queue.pop(0)
        visited[com] = True
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:
                if visited[connect] == False:
                    queue.append(connect)

n, computers = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(solution(n, computers))
"""
1 2 1 3.... 1,n
2, 3


[[1, 1, 0]
 [1, 1, 0]
 [0, 0, 1]]
 
[[1, 1, 0]
 [1, 1, 1]
 [0, 1, 1]]
"""