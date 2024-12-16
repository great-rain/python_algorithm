N, C = map(int, input().split())
score = sorted([int(i) for i in input().split()], reverse=True)
print(score[C-1])