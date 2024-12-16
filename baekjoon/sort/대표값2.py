a = []
for _ in range(5):
    a.append(int(input()))

b = [sum(a)//5, sorted(a)[2]]
print(*b, sep='\n')