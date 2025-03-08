from collections import deque


def solution(prices):
    answer = []
    prices_q = deque(prices)

    while prices_q:
        price = prices_q.popleft()
        time = 0
        for q in prices_q:
            time += 1
            if price > q:
                break
        answer.append(time)
    return answer