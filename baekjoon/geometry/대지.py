n = int(input())
if n == 1:
    print(0)
else:
    x_list = []
    y_list = []
    for _ in range(n):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)
    print((max(x_list) - min(x_list)) * (max(y_list) - min(y_list)))


"""
_, *l = map(int, open(0).read().split()) # 전체 input 값을 List로 받아온다.
x, y= l[::2], l[1::2] # 홀수 index는 X좌표, 짝수 index는 y 좌표
print((max(x)-min(x)) * (max(y)-min(y)))
"""