N = int(input())
li = []
for _ in range(N):
    li.append(int(input()))

# for i in sorted(li):
#     print(i)
print(*sorted(li), sep='\n')