import sys
while True:
    s = sys.stdin.readline().strip()
    if s == '0': break
    i, j = 0, len(s)-1
    flag = True
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            flag = False
            break
    print('yes') if flag else print('no')