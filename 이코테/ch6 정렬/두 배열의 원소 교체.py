"""
5 3
1 2 5 4 3
5 5 6 6 5
"""

N, K = map(int, input().split())
A = sorted(map(int, input().split())) # sorted 함수는 list도 같이 진행해준다.
B = sorted(map(int, input().split()), reverse=True)
for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break
print(sum(A))