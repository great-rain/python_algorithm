N, X = map(int, input().split())
l = list(map(int, input().split()))
print(" ".join(map(str, [i for i in l if i < X])))