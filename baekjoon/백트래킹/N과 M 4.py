def recur(N, M, sequence, start):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    for i in range(start, N+1):
        recur(N, M, sequence + [i], i)

N, M = map(int, input().split())
recur(N, M, [], 1)
