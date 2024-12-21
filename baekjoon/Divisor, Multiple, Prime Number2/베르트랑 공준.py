import sys

prime_list = [0, 0] + [1] * 246912

for i in range(2, 246913):
    if prime_list[i]:
        for j in range(i*2, 246913, i):
            prime_list[j] = 0

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0: break
    print(sum(prime_list[n+1:n*2+1]))