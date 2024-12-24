import sys

Input = sys.stdin.readline

prime = []
numbers = [1, 1] + [0] * 999999
for i in range(2, 1000001):
    if numbers[i] == 0:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            numbers[j] = 1

for _ in range(int(input())):
    count = 0
    N = int(input())
    for i in prime:
        if i >= N:
            break
        if not numbers[N-i] and i <= N-i:
            count += 1
    print(count)

