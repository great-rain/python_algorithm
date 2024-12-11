M = int(input())
N = int(input())

if M == 1: M = 2
min = 0
sum = 0
for i in range(M, N+1):
    prime = True
    for n in range(2, int(i**0.5)+1):
        if i % n == 0:
            prime = False
            break
    if prime:
        sum += i
        if min == 0:
            min = i

if min == 0 and sum == 0:
    print(-1)
else:
    print(sum)
    print(min)