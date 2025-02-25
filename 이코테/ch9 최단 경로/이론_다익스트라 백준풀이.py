from heapq import heappush, heappop
import io, os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

v, e = map(int, input().split())
k = int(input())

adj = [[] for _ in range(v+1)]
d = [200000]*(v+1)

for _ in range(e):
    a, b, w = map(int, input().split())
    adj[a].append((w, b))

d[k] = 0
pq = [(0, k)]
while pq:
    cur_w, cur = heappop(pq)
    if cur_w != d[cur]: continue

    for nxt_w, nxt in adj[cur]:
        if d[cur]+nxt_w < d[nxt]:
            d[nxt] = d[cur]+nxt_w
            heappush(pq, (d[nxt], nxt))

for i in range(1, v+1):
    print(d[i] if d[i] != 200000 else 'INF')