a = 0

for i in range(0,5):
    a += 35 * 36 ** i

print(a)

# 60466175
# 1348621560
'''
35
35 * 36 ^ 1
35 * 36 ^ 2
35 * 36 ^ 3
35 * 36 ^ 4
'''
#
# n,b = input().split()
# digit = len(n); b = int(b); res = 0
# for i in range(digit):
#     check = n[i]
#     if 'A' <= check <= 'Z':
#         res += int((ord(check) - 55)) * (b**(digit-i-1))
#     else:
#         res += int(check) * (b**(digit-i-1))
# print(res)

"""
n,b=input().split()
print(int(n,int(b)))
"""
print(int('A', 36))
"""
파이썬에서 진법 변환을 통해 문자열로 표현된 수를 정수(int)로 변환하려면 내장 함수 int()를 사용할 수 있습니다. int() 함수는 숫자 문자열과 진법을 받아 정수를 반환합니다. 
이를 통해 다양한 진법에서 10진수로 변환이 가능합니다.

기본 사용법
int(x, base)
x: 변환하고자 하는 숫자 문자열.
base: 숫자가 표현된 진법(2에서 36 사이의 값).
"""