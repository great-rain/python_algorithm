"""
1/1(1)
1/2(2), 2/1(3)
3/1(4), 2/2(5), 1/3(6)
1/4(7), 2/3(8), 3/2(9), 4/1(10)
5/1(11), 4/2(12), 3/3(13), 2/4(14), 1/5(15)

짝수 분모 - 1 분자 + 1
짝수 분모 + 1 분자 - 1
"""

num = 14 # int(input())
line = 1

while num > line:
    num -= line
    line += 1

# 짝수일경우
if line % 2 == 0:
    a = num
    b = line - num + 1
# 홀수일경우
elif line % 2 == 1:
    a = line - num + 1
    b = num

print(f'{a}/{b}')
