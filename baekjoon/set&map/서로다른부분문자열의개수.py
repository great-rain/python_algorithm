N = input()
a = {}
for i in range(1, len(N)+1):
    for j in range(0, len(N)):
        w = N[j:j+i]
        if a.get(w, False):
            continue
        else:
            a[w] = True

print(len(a))
