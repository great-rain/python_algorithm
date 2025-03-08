from collections import deque


def solution(priorities, location):
    dq = deque()
    result = {}
    result_idx = 1
    for i in range(len(priorities)):
        dq.append((priorities[i], i))

    while dq:
        max_priority, max_idx = max(dq)
        priority, idx = dq.popleft()
        if priority < max_priority:
            dq.append((priority, idx))
        else:
            result[idx] = result_idx
            result_idx += 1

    return result[location]

priorities, location = [2, 1, 3, 2],2
print(solution(priorities, location))