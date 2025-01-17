def generate_sequences(N, M, sequence, visited):
    if len(sequence) == M:
        print(" ".join(map(str, sequence)))
        return

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            generate_sequences(N, M, sequence + [i], visited)
            visited[i] = False

N, M = map(int, input().split())

visited = [False] * (N + 1)
generate_sequences(N, M, [], visited)