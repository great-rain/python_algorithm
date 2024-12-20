N = int(input())

trees = []
diff = []
for _ in range(N):
    trees.append(int(input()))

for i in range(N-1):
    diff.append(trees[i+1]-trees[i])

# diff 의 공약수 구해서 사이에 몇개 들어가야되는지 확인