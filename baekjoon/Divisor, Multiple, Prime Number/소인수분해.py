# N = int(input())
# factor = 2
#
# while factor <= N:
#     if N % factor == 0:
#         print(factor)
#         N /= factor
#     else:
#         factor += 1


import sys

n = int(sys.stdin.readline())
while n % 2 == 0:
    print(2)
    n //= 2

# Step 2: Handle odd factors from 3 onwards
factor = 3
while factor * factor <= n:
    while n % factor == 0:
        print(factor)
        n //= factor
    factor += 2

# Step 3: If n is a prime number greater than 2
if n > 1:
    print(n)
