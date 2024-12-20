import sys
P = sys.stdout.write
N = int(sys.stdin.readline())
gcd = []
for i in range(2, int(N**0.5)+1):
    while N%i == 0:
        gcd.append(i)
        N //= i

if N != 1: gcd.append(N) # 소수처리
P(str(len(gcd))+' \n')
P(' '.join(map(str, gcd)))