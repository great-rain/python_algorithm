fx, fc = map(int, input().split())
c = int(input())
n = int(input())
if (fx * n + fc) <= (c*n) and fx <= c:
    print(1)
else:
    print(0)