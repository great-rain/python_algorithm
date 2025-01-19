N, M = map(int, input().split())
def recur(N, M, sequence):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    for i in range(1, N+1):
        recur(N, M, sequence + [i])

recur(N, M, [])