def fivonachi(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fivonachi(n-1) + fivonachi(n-2)

print(fivonachi(17))