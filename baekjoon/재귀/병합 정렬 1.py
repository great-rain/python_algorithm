def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)

def merge(arr, p, q, r):
    global count, res

    tmp = []
    i, j = p, q + 1

    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1

        else:
            tmp.append(arr[j])
            j += 1

    while i <= q:
        tmp.append(arr[i])
        i += 1

    while j <= r:
        tmp.append(arr[j])
        j += 1

    i = p
    t = 0

    while i <= r:
        arr[i] = tmp[t]
        count += 1
        if count == K:
            res = arr[i]
            break
        i += 1
        t += 1

A, K = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
res = -1
merge_sort(arr, 0, A - 1)
print(res)
