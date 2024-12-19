N,M = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))
print(len(A ^ B))

# n,m = map(int, input().split())
# a = {i:'' for i in input().split()}
# b = input().split()
# cnt=0
# for i in range(m):
#     if b[i] in a:
#         cnt += 1
#
# print(len(a)+len(b)-2*cnt)