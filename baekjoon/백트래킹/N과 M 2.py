N, M = map(int, input().split())

visited = [False] * (N+1)

def recur(N, M, sequence, visited, stack):
    if len(sequence) == M:
        if sorted(sequence) in stack:
            return
        else:
            stack.append(sorted(sequence))
            print(" ".join(map(str, sequence)))
            return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            recur(N, M, sequence + [i], visited, stack)
            visited[i] = False

recur(N, M, [], visited, [])