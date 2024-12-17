import sys
I = sys.stdin.readline
N = int(I())
a = []
for _ in range(N):
    item = I()
    if item not in a:
        a.append(item)

def recursive_sort(a:list):
    # 리스트가 비어있으면 빈 튜플 반환 (종료 조건)
    if not a:
        return ()
    # 첫 요소와 나머지를 재귀적으로 호출
    return (len(a), a[0]) + recursive_sort(a[1:])


a.sort(key=recursive_sort)
for i in a:
    sys.stdout.write(i)


# import sys
# n = int(sys.stdin.readline())
# words = list(set([sys.stdin.readline().strip() for _ in range(n)]))
# words.sort()
# print('\n'.join(sorted(words, key=len)))