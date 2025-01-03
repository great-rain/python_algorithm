import sys
Input = sys.stdin.readline

def find_room(H, W, N):
    count = 1
    for i in range(1, W + 1):
        for j in range(1, H + 1):
            if count == N:
                if i < 10:
                    return str(j) + '0' + str(i)
                return str(j) + str(i)
            count += 1

for _ in range(int(Input())):
    H, W, N = map(int, input().split())
    print(find_room(H, W, N))