X = int(input())
N = int(input())

for _ in range(N):
    p, c = map(int, input().split())
    X -= p * c

print("Yes") if X == 0 else print("No")