import sys
Input = sys.stdin.readline
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(int(Input())):
    n = int(Input())
    while True:
        if is_prime(n):
            print(n)
            break
        else:
            n += 1