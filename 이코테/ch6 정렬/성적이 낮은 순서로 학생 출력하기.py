'''
2
홍길동 95
이순신 77
'''

N = int(input())

arr = []
for _ in range(N):
    data = input().split()
    arr.append((data[0], data[1]))

arr.sort(key=lambda x: int(x[1]))

for s in arr:
    print(s[0], end=' ')