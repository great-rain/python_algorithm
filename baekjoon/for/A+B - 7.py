import sys

num = int(input())
for i in range(1, num+1):
    a, b = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {a+b}")