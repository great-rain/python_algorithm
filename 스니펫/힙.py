import heapq

# 최소 힙 예시
min_heap = []
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 7)
print("최소 힙:", min_heap)
print("최솟값:", heapq.heappop(min_heap))

# 최대 힙 예시
max_heap = []
heapq.heappush(max_heap, -4)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -7)
print("최대 힙:", [-x for x in max_heap])
print("최댓값:", -heapq.heappop(max_heap))
