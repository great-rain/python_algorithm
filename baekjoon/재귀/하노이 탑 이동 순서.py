def hanoi(n, start, target, auxiliary, arr=[]):
    if n == 1:
        arr.append([start, target])
        return arr
    hanoi(n - 1, start, auxiliary, target, arr)
    arr.append([start, target])
    hanoi(n - 1, auxiliary, target, start, arr)

    return arr

res = hanoi(int(input()),'1','3','2')

print(len(res))
for i in res:
    print(' '.join(i))