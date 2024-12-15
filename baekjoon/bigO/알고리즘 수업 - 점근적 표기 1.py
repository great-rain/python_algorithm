fx, fc = map(int, input().split())
c = int(input())
n = int(input())
if (fx-c) * n + fc <= 0:
    print(1)
else:
    print(0)