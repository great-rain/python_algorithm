prime = []
numbers = [1, 1] + [0] * 999999

for i in range(2, 1000001):
    if numbers[i] == 0:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            numbers[j] = 1

N, M = map(int, input().split())
for p in prime:
    if N <= p <= M:
        print(p)
    elif p > M:
        break
